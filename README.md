# E-commerce AI Agent (RAG-based)

## 📌 Overview

This project is an AI-powered assistant that answers customer queries related to e-commerce policies (returns, refunds, shipping) using Retrieval-Augmented Generation (RAG).

Instead of guessing answers, the system retrieves relevant information from documents and provides accurate responses with citations.

---

## ⚙️ Features

* Semantic search using embeddings
* Vector database (FAISS)
* Intelligent decision-making (APPROVED / DENIED)
* Source-based answers (no hallucination)

---

## 🛠️ Tech Stack

* Python
* LangChain
* FAISS
* HuggingFace Embeddings

---

## 📂 Project Structure

```
ecommerce-ai-agent/
│
├── main.py
├── data/
│   ├── refunds.txt
│   ├── returns.txt
│   └── shipping.txt
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the project:

```
python main.py
```

---

## 💡 Example Query

```
Can I return damaged item?
```

## ✅ Output

* Decision (APPROVED / DENIED)
* Reason
* Citations from source files

---

## 🚀 Future Improvements

* Add UI (Streamlit)
* Use real OpenAI API
* Improve decision logic
