from agents.base_agent import BaseAgent


class PortfolioAgent(BaseAgent):

    def __init__(self):

        super().__init__("Portfolio Agent")

    def summarize(self):

        return {

            "Portfolio Value": "$150 Million",

            "Technology": "42%"

        }