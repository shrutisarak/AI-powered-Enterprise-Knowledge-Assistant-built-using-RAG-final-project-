import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/sops"
DB_PATH = "vectorstore"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50


def split_text(text):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + CHUNK_SIZE
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - CHUNK_OVERLAP

    return chunks


def ingest_documents():
    texts = []

    for file in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, file)

        if file.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            docs = loader.load()
            for d in docs:
                texts.extend(split_text(d.page_content))

        elif file.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf-8")
            docs = loader.load()
            for d in docs:
                texts.extend(split_text(d.page_content))

    if not texts:
        print("❌ No SOP documents found.")
        return

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(texts, embeddings)
    vectorstore.save_local(DB_PATH)

    print("✅ SOP documents ingested and vector store created successfully.")


if __name__ == "__main__":
    ingest_documents()
