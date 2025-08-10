# 📄 Azure HR Copilot – PDF Page Splitter Function

An **Azure Function** that:
- Receives a PDF (via HTTP request from Power Automate or other apps)
- Splits it into **page-level PDFs**
- Uploads them to **Azure Blob Storage**
- Cleans up any older page files for the same document

Designed for **Retrieval-Augmented Generation (RAG)** pipelines where fine-grained document search is needed.

---

## 🚀 Features
- **Two endpoints**:
  1. **`split-pdf`** → Split PDF into pages & upload to Blob Storage
  2. **`delete-pdf-pages`** → Remove all page files for a given document
- **Blob Storage integration**
- **Power Automate friendly**
- **Modular** for use in larger AI search/chat pipelines

---

## 📂 Folder Structure
```plaintext
functions/
└── pdf-page-splitter/
    ├── __init__.py         # Main Azure Function logic
    ├── function.json       # Trigger & binding configuration
    ├── requirements.txt    # Python dependencies
    └── README.md           # (Optional) Function-specific doc

**Note**: `delete-pdf-pages` is available but not used in the default Power Automate workflow for this project.
