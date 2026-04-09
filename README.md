# Fitness Knowledge API (Local RAG System)

A local Retrieval-Augmented Generation (RAG) API built using TinyLlama, ChromaDB, LangChain, and FastAPI.

This system answers fitness-related questions using a private knowledge base without requiring any external LLM APIs.

---

## Features

- Fully local LLM inference (no OpenAI required)
- Vector search using ChromaDB
- Retrieval-Augmented Generation pipeline
- FastAPI inference endpoint
- Runs entirely offline
- Lightweight model (TinyLlama GGUF)

---

## Architecture

User Query
   ↓
Embedding Model
   ↓
ChromaDB Vector Search
   ↓
Context Retrieval
   ↓
TinyLlama Local LLM
   ↓
Generated Answer

---

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- llama-cpp-python
- TinyLlama (GGUF format)

---

## Project Structure

fitness-knowledge-api/
│
├── app.py # FastAPI inference server
├── ingest.py # document ingestion pipeline
├── docs/ # knowledge base
├── chroma_db/ # vector store (generated locally)
├── models/ # local GGUF model (ignored in git)
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1. Clone repo

git clone 
cd fitness-knowledge-api

### 2. Create environment

python -m venv venv
source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add local model

Download TinyLlama GGUF:

models/tinyllama.gguf

---

## Build Vector Database

python ingest.py

---

## Run API

uvicorn app:app –reload

Open: http://127.0.0.1:8000/docs

---

## Example Query

POST /ask

{
“question”: “How much protein should I eat daily?”
}

---

## Why Local RAG?

Most LLM applications rely on cloud APIs.

This project demonstrates:

- offline inference
- private knowledge retrieval
- low-resource deployment
- reproducible vector pipelines

This architecture is useful for:

- healthcare assistants
- enterprise knowledge bots
- offline education tools
- privacy-sensitive applications

---

## Future Improvements

- switch TinyLlama → Mistral 7B
- streaming responses
- multi-document ingestion
- Docker deployment
- evaluation pipeline

