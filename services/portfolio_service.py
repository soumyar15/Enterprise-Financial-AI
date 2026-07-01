from database.models import Portfolio


class PortfolioService:

    def get_summary(self):

        return {
            "portfolio_name": "Global Equity Fund",
            "aum": "150 Million USD",
            "number_of_holdings": 248,
            "tracking_error": 2.31,
            "active_risk": 4.18,
            "var": "2.3 Million USD"
        }

    def get_top_holdings(self):

        return [

            {"ticker": "AAPL", "weight": 7.2},

            {"ticker": "MSFT", "weight": 6.5},

            {"ticker": "NVDA", "weight": 5.8}

        ]