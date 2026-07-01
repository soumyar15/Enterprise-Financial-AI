from llm.llm_manager import LLMManager

manager = LLMManager()


class LLMService:

    def ask(self, question):

        return manager.generate(question)