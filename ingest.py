import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


DOCS_PATH = "docs"
CHROMA_PATH = "chroma_db"


def load_documents():
    documents = []

    for filename in os.listdir(DOCS_PATH):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(DOCS_PATH, filename))
            documents.extend(loader.load())

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_documents(documents)


def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    vector_store.persist()

    print("Vector DB created successfully")


def main():

    print("Loading documents...")
    documents = load_documents()

    print("Splitting documents...")
    chunks = split_documents(documents)

    print("Generating embeddings...")
    create_vector_store(chunks)


if __name__ == "__main__":
    main()