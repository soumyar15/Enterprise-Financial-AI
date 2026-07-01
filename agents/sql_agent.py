from agents.base_agent import BaseAgent


class SQLAgent(BaseAgent):

    def __init__(self):

        super().__init__("SQL Agent")

    def execute_query(self):

        return {

            "Rows Returned": 125

        }