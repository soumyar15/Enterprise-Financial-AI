from agents.portfolio_agent import PortfolioAgent
from agents.risk_agent import RiskAgent
from agents.market_agent import MarketAgent
from agents.news_agent import NewsAgent
from agents.document_agent import DocumentAgent


class AgentOrchestrator:

    def __init__(self):

        self.portfolio = PortfolioAgent()

        self.risk = RiskAgent()

        self.market = MarketAgent()

        self.news = NewsAgent()

        self.document = DocumentAgent()