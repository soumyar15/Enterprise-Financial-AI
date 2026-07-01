from agents.base_agent import BaseAgent


class RiskAgent(BaseAgent):

    def __init__(self):

        super().__init__("Risk Agent")

    def calculate_var(self):

        return {

            "Portfolio VaR": "$2.3 Million",

            "Confidence": "95%",

            "Holding Period": "1 Day"

        }