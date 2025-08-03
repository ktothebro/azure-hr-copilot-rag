Azure HR Copilot – RAG Architecture
📌 Overview
Azure HR Copilot is an AI-powered chatbot that provides instant, grounded answers to HR policy and procedure questions.
It uses a Retrieval-Augmented Generation (RAG) architecture built on Azure AI services, with secure, enterprise-ready integration and low-code orchestration.

This public-safe replica uses synthetic HR documents to demonstrate the same architecture and workflow used in production.

🏗 Architecture

Workflow:

Power Automate Flow detects new HR documents in SharePoint.

Documents are sent to Azure Blob Storage.

Azure Function App splits PDFs into page-level documents for cost-efficient semantic search.

Azure AI Search indexes each page for precise retrieval.

Azure OpenAI Service (GPT-3.5/4 Turbo) uses RAG to ground answers in indexed content.

Responses are delivered to users via Power Automate and Copilot Studio.

⚙️ Tech Stack
Azure Blob Storage – document storage

Azure AI Search – indexing & semantic retrieval

Azure OpenAI Service – GPT-3.5/4 Turbo for generative responses

Power Automate – low-code orchestration

Azure Function App – PDF ingestion & page-splitting

SharePoint – HR document source

🚀 Setup & Installation
Prerequisites
Azure subscription

Azure OpenAI resource with GPT-3.5/4 Turbo deployment

Azure AI Search resource

Azure Blob Storage container

Power Automate environment

1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/yourusername/azure-hr-copilot-rag.git
cd azure-hr-copilot-rag
2. Configure Environment
Create a .env file (see .env.example) with:

ini
Copy
Edit
AZURE_OPENAI_KEY=your_key
AZURE_SEARCH_KEY=your_key
BLOB_CONNECTION_STRING=your_connection_string
3. Deploy Azure Function App
Deploy from functions/pdf-page-splitter

Function automatically chunks PDFs into page-level files and uploads to Blob Storage.

4. Import Power Automate Flow
Import the flows/hr-copilot.zip file into your environment.

Update connections for Blob Storage and Azure OpenAI.

📂 Repository Structure
bash
Copy
Edit
azure-hr-copilot-rag/
│
├── functions/
│   └── pdf-page-splitter/     # Azure Function App code for PDF chunking
│
├── sample-data/
│   └── hr-handbook.pdf        # Synthetic HR policy document
│
├── flows/
│   └── hr-copilot.zip         # Exported Power Automate Flow
│
├── docs/
│   └── architecture.png       # Architecture diagram
│
├── .gitignore
├── LICENSE
└── README.md
📝 Features
Retrieval-Augmented Generation (RAG) over HR documents

Secure integration with Azure services

Fine-grained page-level search for reduced cost and higher precision

Low-code + code hybrid architecture

📊 Example Query
User: "What is the company’s parental leave policy?"
Bot: "Eligible employees receive up to 12 weeks of parental leave as outlined in page 14 of the HR Handbook (v2025)."

🔒 Data Privacy
All documents in this repo are synthetic and do not contain any proprietary or confidential information.

