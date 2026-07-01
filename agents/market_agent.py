from agents.base_agent import BaseAgent


class MarketAgent(BaseAgent):

    def __init__(self):

        super().__init__("Market Agent")

    def market_summary(self):

        return {

            "Market": "Bullish",

            "Volatility": "Moderate"

        }