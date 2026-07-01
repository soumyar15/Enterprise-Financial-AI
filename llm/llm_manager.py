class LLMManager:

    def __init__(self):

        self.provider = "Azure OpenAI"

    def generate(self, prompt):

        return {

            "provider": self.provider,

            "response": "LLM response placeholder"

        }