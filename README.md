# 🏢 Enterprise RAG-Based SOP Assistant

An **Enterprise Knowledge Assistant** built using **Retrieval-Augmented Generation (RAG)** to query **company SOP (Standard Operating Procedure) documents**.  
The system retrieves relevant SOP sections using **semantic search** and provides **accurate, hallucination-free answers**.

---

## 📌 Problem Statement
Enterprises store SOPs across multiple documents (HR, IT, Finance, Onboarding).  
Employees often struggle to:
- Quickly find correct SOP information
- Avoid outdated or irrelevant policies
- Get clear answers from lengthy documents

Traditional keyword search is inefficient and error-prone.

---

## 💡 Solution
This project implements a **RAG-based SOP Assistant** that:
- Ingests SOP documents
- Converts them into vector embeddings
- Stores them in a FAISS vector database
- Retrieves the most relevant SOP content
- Extracts clean, policy-grounded answers
- Avoids hallucinations for out-of-scope questions

---

## 🧠 Key Features
- 📄 SOP document ingestion (HR, IT, Finance, Onboarding)
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- 🚫 No hallucination (out-of-scope detection)
- ⚡ Fast FAISS-based similarity search
- 🖥️ Simple Streamlit web interface
- 🔌 Offline & exam-safe (no API keys required)

---

## 🛠️ Technology Stack

| Layer | Technology |
|-----|-----------|
| Programming Language | Python |
| UI | Streamlit |
| Embeddings | Sentence-Transformers |
| Vector Database | FAISS |
| Document Parsing | PyPDF, TextLoader |
| Architecture | RAG (Retrieval-Augmented Generation) |

---

## 📂 Project Structure
Enterprise_RAG_SOP_Assistant/
│
├── data/
│ └── sops/
│ ├── hr_policy.txt
│ ├── it_security.txt
│ ├── finance_sop.txt
│ └── onboarding_sop.txt
│
├── ingest.py # SOP ingestion & vector creation
├── retriever.py # FAISS retriever
├── rag_chain.py # RAG logic & answer extraction
├── app.py # Streamlit UI
├── requirements.txt
└── README.md

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Add SOP Documents
Place SOP text files inside:

bash
Copy code
data/sops/
🚀 Running the Application
Step 1: Ingest SOP Documents
bash
Copy code
python ingest.py
Expected output:

cpp
Copy code
✅ SOP documents ingested and vector store created successfully.
Step 2: Run the Web App
bash
Copy code
streamlit run app.py
Open in browser:

arduino
Copy code
http://localhost:8501
🧪 Sample Questions
HR SOP
How many casual leaves are allowed per year?

Is medical certificate required for sick leave?

What is the emergency leave process?

IT Security SOP
How do I report a security incident?

What are the steps in incident response?

Finance SOP
What expenses are eligible for reimbursement?

How long does reimbursement take?

Onboarding SOP
What happens on the first day of onboarding?

Who prepares system access for new employees?

Out-of-Scope (Handled Correctly)
What is the salary structure?

What is the resignation process?

Expected response:

arduino
Copy code
❌ Answer not available in SOP.
🧠 System Workflow
SOP documents are loaded and chunked

Text is converted into vector embeddings

Embeddings are stored in FAISS

User question is converted to embedding

Relevant SOP chunks are retrieved

Clean answer is extracted from SOP content

🎯 Use Cases
Employee self-service SOP assistant

HR policy query system

IT helpdesk knowledge assistant

Finance & compliance support

Onboarding guidance system

🚫 Hallucination Prevention
Answers are generated only from SOP content

If no relevant SOP exists, system responds clearly

No external LLM inference used in demo version

📈 Future Enhancements
LLM-based summarization (ChatGPT / LLaMA)

SOP source citation

Role-based access control

Upload SOPs via UI

Chat history & confidence scoring

Integration with Slack / Teams

