from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
import os

print("STARTING AI...")

# API key
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# Load file
from langchain_community.document_loaders import DirectoryLoader

# Load ALL files from data folder
loader = DirectoryLoader("data/", glob="*.txt")
documents = loader.load()

print("Loaded all documents")

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
docs = text_splitter.split_documents(documents)

print("Chunks created")

# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Store in FAISS
db = FAISS.from_documents(docs, embeddings)

print("Vector DB ready")

# Query
query = input("Ask your question: ")

results = db.similarity_search(query)

print("\n--- RESPONSE ---")

if results:
    top_results = results[:2]   # only most relevant

decision = "APPROVED ✅"
q = query.lower()

# First pass → check approval
for r in top_results:
    text = r.page_content.lower()
    if "damaged" in q and "eligible" in text:
        decision = "APPROVED ✅"
        break

# Second pass → check denial ONLY if needed
if decision != "APPROVED ✅":
    for r in top_results:
        text = r.page_content.lower()
        if "food" in q and "not allowed" in text:
            decision = "DENIED ❌"
            break
        if "opened" in q and "not eligible" in text:
            decision = "DENIED ❌"
            break

print(f"Decision: {decision}\n")

print("Reason:")
for r in results[:2]:
    print("-", r.page_content)

print("\nCitations:")
for r in results[:2]:
    source = r.metadata.get("source", "unknown")
    print("-", source)