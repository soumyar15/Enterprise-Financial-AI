from rag.pipeline import RAGPipeline


rag = RAGPipeline()


class RAGService:

    def answer(self, question):

        return rag.query(question)