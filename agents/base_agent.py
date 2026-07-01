class BaseAgent:

    def __init__(self, name):

        self.name = name

    def execute(self, query):

        return {
            "agent": self.name,
            "query": query,
            "status": "Executed"
        }