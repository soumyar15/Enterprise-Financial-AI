import chromadb


client = chromadb.PersistentClient(path="./vectorstore")


collection = client.get_or_create_collection(
    "finance_documents"
)