from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

DB_PATH = "data/vector_db"

# embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def process_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = splitter.split_documents(documents)

    db = FAISS.from_documents(docs, embeddings)
    db.save_local(DB_PATH)


def load_vector_db():
    if os.path.exists(DB_PATH):
        return FAISS.load_local(
            DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
    return None


def search_pdf(query):

    db = load_vector_db()

    if db is None:
        return ""

    docs = db.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])
    return context