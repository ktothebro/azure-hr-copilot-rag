import logging
import azure.functions as func
import fitz  # PyMuPDF
from azure.storage.blob import BlobServiceClient
import os

app = func.FunctionApp()

# 🧹 1. Delete Pages Function
@app.function_name(name="DeletePDFPages")
@app.route(route="delete-pdf-pages", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def delete_pdf_pages(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        filename = req_body.get("filename")
        if not filename:
            return func.HttpResponse("Missing filename", status_code=400)

        blob_conn_str = os.environ["AzureWebJobsStorage"]
        container_name = "hr-documents"
        blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)
        container_client = blob_service_client.get_container_client(container_name)

        deleted = 0
        for blob in container_client.list_blobs(name_starts_with=filename + "_page_"):
            container_client.delete_blob(blob.name)
            deleted += 1

        return func.HttpResponse(f"✅ Deleted {deleted} page(s) for {filename}", status_code=200)

    except Exception as e:
        logging.exception("❌ Deletion error")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)

# 📄 2. Split PDF Function
@app.function_name(name="SplitPDFByPage")
@app.route(route="split-pdf", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def split_pdf_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("⚙️ PDF Split Function triggered.")

    try:
        pdf_bytes = req.get_body()
        if not pdf_bytes:
            return func.HttpResponse("❌ No file uploaded", status_code=400)

        filename = req.headers.get("x-filename") or req.params.get("filename") or "uploaded_file"

        # Split PDF
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        pages = []
        for page_number in range(len(doc)):
            new_pdf = fitz.open()
            new_pdf.insert_pdf(doc, from_page=page_number, to_page=page_number)
            page_bytes = new_pdf.write()
            pages.append((page_number + 1, page_bytes))

        # Upload to Azure Blob
        blob_conn_str = os.environ["AzureWebJobsStorage"]
        container_name = "hr-documents"
        blob_service_client = BlobServiceClient.from_connection_string(blob_conn_str)
        container_client = blob_service_client.get_container_client(container_name)

        # 🔥 Delete previous pages for this file
        logging.info(f"🧹 Cleaning up old blobs for: {filename}_page_*")
        for blob in container_client.list_blobs(name_starts_with=f"{filename}_page_"):
            container_client.delete_blob(blob.name)
            logging.info(f"🗑️ Deleted: {blob.name}")
        
        # Upload new pages
        uploaded = []
        for page_number, page_bytes in pages:
            blob_name = f"{filename}_page_{page_number}.pdf"
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
            blob_client.upload_blob(page_bytes, overwrite=True)
            uploaded.append(blob_name)

        return func.HttpResponse(f"✅ Uploaded {len(uploaded)} pages", status_code=200)

    except Exception as e:
        logging.exception("❌ Error during processing")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
