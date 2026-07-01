from app.router import AgentRouter

router = AgentRouter()


class QueryService:

    def process(self, question):

        return router.route(question)