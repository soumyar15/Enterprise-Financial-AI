from langgraph.graph import StateGraph

from agents.portfolio_agent import PortfolioAgent
from agents.risk_agent import RiskAgent
from agents.research_agent import ResearchAgent


class WorkflowState(dict):
    pass


portfolio = PortfolioAgent()
risk = RiskAgent()
research = ResearchAgent()


def portfolio_node(state):
    state["portfolio"] = portfolio.summarize()
    return state


def risk_node(state):
    state["risk"] = risk.calculate_var()
    return state


def research_node(state):
    state["research"] = research.analyse("Apple")
    return state


builder = StateGraph(WorkflowState)

builder.add_node("portfolio", portfolio_node)
builder.add_node("risk", risk_node)
builder.add_node("research", research_node)

builder.set_entry_point("portfolio")
builder.add_edge("portfolio", "risk")
builder.add_edge("risk", "research")

graph = builder.compile()