from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_cpp import Llama


CHROMA_PATH = "chroma_db"
MODEL_PATH = "models/tinyllama.gguf"


app = FastAPI()


class QueryRequest(BaseModel):
    question: str


print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Loading vector database...")
vector_store = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embeddings
)

print("Loading Mistral model...")
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048
)


@app.post("/ask")
def ask_question(request: QueryRequest):

    docs = vector_store.similarity_search(request.question, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{request.question}

Answer:
"""

    #output = llm(prompt, max_tokens=200)
    output = llm.create_completion( prompt = prompt, max_tokens = 200, temperature = 0.7)

    return {
        "answer": output["choices"][0]["text"].strip()
    }