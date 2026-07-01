from rag.retriever import RAGRetriever


class RAGPipeline:

    def __init__(self):

        self.retriever = RAGRetriever()

    def query(self, question):

        context = self.retriever.search(question)

        return {

            "question": question,

            "context": context

        }