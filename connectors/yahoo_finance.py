import yfinance as yf


class YahooConnector:

    def price(self, ticker):

        return yf.Ticker(ticker).history(period="1d")