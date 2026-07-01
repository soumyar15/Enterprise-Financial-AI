from agents.base_agent import BaseAgent


class DocumentAgent(BaseAgent):

    def __init__(self):

        super().__init__("Document Agent")

    def analyse_document(self):

        return {

            "Status": "Completed"

        }