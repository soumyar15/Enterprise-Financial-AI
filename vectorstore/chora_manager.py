import chromadb


client = chromadb.PersistentClient("./vectorstore")


collection = client.get_or_create_collection(

    "enterprise_finance"

)