# Fitness Knowledge Retrieval API

This project implements a local Retrieval-Augmented Generation (RAG) pipeline using a quantized Mistral model served via Ollama.

The system exposes a FastAPI endpoint that answers fitness-related queries using semantic search over embedded training documents stored in ChromaDB.

## Architecture

Documents → Chunking → Embeddings → ChromaDB → Retriever → Mistral (local) → FastAPI endpoint

## Status

Project under active development.
