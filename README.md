# UNG Handbook Chatbot – Azure RAG Demo
[Live Demo]([https://ktothebro.github.io/hr-chatbot-demo-azure-RAG/](https://ktothebro.github.io/hr-chatbot-demo-azure-RAG/))
## 📌 Overview
This project demonstrates a **Retrieval-Augmented Generation (RAG) chatbot** using **Azure AI services**.  
It answers questions based on the **University of North Georgia (UNG) Student Handbook 2024-2025**.

This **public-safe demo** replicates the architecture and workflow used in enterprise HR projects but uses only **synthetic or public data**, so no confidential HR information is exposed.

---

## 🏗 Architecture
![Architecture Diagram](docs/architecture.png)

**Workflow:**
1. **GitHub Pages frontend** collects user questions.
2. Requests are sent to a **Power Automate HTTP Trigger**.
3. (Optional) **Azure Function App** can preprocess text or split documents into pages.
4. **Azure AI Search** indexes handbook pages for semantic retrieval.
5. **Azure OpenAI Service** (GPT-3.5/4) generates answers grounded in the indexed content.
6. Responses are returned to the frontend via **HTTP Response**.

---

## ⚙️ Tech Stack
- **GitHub Pages** – demo frontend hosting  
- **HTML/JS** – chat interface  
- **Power Automate** – orchestrates HTTP requests  
- **Azure AI Search** – semantic indexing of handbook pages  
- **Azure OpenAI Service** – GPT-3.5/4 for RAG-based responses  
- **Azure Function App** – optional document/page preprocessing  

---

## 📄 Project Notes
The original HR Copilot project at **Affirma Consulting** included:

- **Delete Function (`delete-pdf-pages`)**: Tested, works, but not integrated into the flow; useful for manual cleanup.  
- **Split Function (`split-pdf`)**: Supports replacement by deleting old page blobs before uploading new ones.

For this **UNG demo**:

- All documents are public, so **manual deletion is not required**.  
- The HTTP-triggered flow is configured for demo-safe queries.  
- You can simulate queries and responses using **sample handbook content**.

---

## 🚀 Setup & Installation

### Prerequisites
- GitHub account
- GitHub Pages enabled for the repository
- Optional: Azure subscription to replicate the full RAG workflow

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ung-handbook-chatbot.git
cd ung-handbook-chatbot
