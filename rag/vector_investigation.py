from rag.document_loader import DocumentLoader
from rag.text_splitter import splitter


class VectorIngestion:

    def ingest(self, pdf):

        docs = DocumentLoader().load(pdf)

        return splitter.split_documents(docs)