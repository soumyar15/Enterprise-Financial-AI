from langchain_openai import AzureChatOpenAI
from config.settings import settings


class AzureOpenAIManager:

    def __init__(self):

        self.llm = AzureChatOpenAI(

            azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,

            api_key=settings.AZURE_OPENAI_API_KEY,

            api_version="2024-02-15-preview",

            deployment_name="gpt-4o"

        )

    def invoke(self, prompt):

        return self.llm.invoke(prompt)