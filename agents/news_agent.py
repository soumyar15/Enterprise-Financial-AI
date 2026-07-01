from agents.base_agent import BaseAgent


class NewsAgent(BaseAgent):

    def __init__(self):

        super().__init__("News Agent")

    def latest_news(self):

        return {

            "Headline": "Market rallies on positive earnings"

        }