from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    def __init__(self):

        super().__init__("Research Agent")

    def analyse(self, company):

        return {

            "company": company,

            "rating": "Buy"

        }