# Project Report: E-commerce AI Agent

## Objective

The goal of this project is to build an AI system that can answer customer queries related to e-commerce policies using document-based retrieval instead of generating random answers.

## Approach

The system uses Retrieval-Augmented Generation (RAG):

1. Documents are loaded from text files.
2. They are split into chunks.
3. Embeddings are created using HuggingFace model.
4. FAISS vector database stores embeddings.
5. User query is matched with similar content.
6. System returns relevant answers with citations.

## Decision Logic

The system determines whether a request is APPROVED or DENIED based on keywords:

* "eligible" → APPROVED
* "not allowed" → DENIED

## Tools Used

* Python
* LangChain
* FAISS
* HuggingFace Embeddings

## Result

The system successfully retrieves relevant policy information and provides accurate answers without hallucination.

## Conclusion

This project demonstrates how AI can be used in real-world applications like customer support using RAG architecture.
