from langchain_community.document_loaders import PyPDFLoader


class DocumentLoader:

    def load(self, pdf):

        loader = PyPDFLoader(pdf)

        return loader.load()