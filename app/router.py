from agents.portfolio_agent import PortfolioAgent
from agents.risk_agent import RiskAgent
from agents.research_agent import ResearchAgent


portfolio = PortfolioAgent()

risk = RiskAgent()

research = ResearchAgent()


class AgentRouter:

    def route(self, question):

        question = question.lower()

        if "risk" in question:

            return risk.calculate_var()

        if "portfolio" in question:

            return portfolio.summarize()

        return research.analyse(question)