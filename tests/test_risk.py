from agents.risk_agent import RiskAgent


def test_var():

    agent = RiskAgent()

    assert agent.calculate_var() is not None