from agents.risk_agent import RiskAgent


agent = RiskAgent()


class RiskService:

    def var(self):

        return agent.calculate_var()