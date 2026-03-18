'''This module will handle market price queries.

Examples:
	•	Last traded price (LTP)
	•	Quotes
	•	Candle data (OHLC)
	•	Historical data
    '''

from execution.fyers_client import FyersClient
from utils.normalize_symbol import normalize_symbol
from datetime import datetime, timedelta

class MarketData:

    def __init__(self, broker=None):
        """Initialize the market data service with an optional broker client."""
        self.broker = broker if broker else FyersClient()

    def _get_quote_values(self, symbol):
        """Fetch the quote payload for a symbol and return its value dictionary."""
        quotes = self.broker.get_quotes(normalize_symbol(symbol))
        quote_items = quotes.get("d", [])
        if not quote_items:
            return {}
        return quote_items[0].get("v", {})
    
    def get_quotes(self, symbol):
        """Return the raw quote response for the given symbol."""
        return self.broker.get_quotes(normalize_symbol(symbol))
    
    def get_ltp(self, symbol):
        """Return the last traded price for the given symbol."""
        data = self._get_quote_values(symbol)
        return data.get("lp")

    def get_bid_ask(self, symbol):
        """Return the current bid and ask prices for the given symbol."""
        data = self._get_quote_values(symbol)
        return {
            "bid_price" : data.get("bid"),
            "ask_price" : data.get("ask"),
        }
    
    def get_candle_data(self, symbol):
        """Return candle data for the given symbol via the broker client."""
        return self.broker.get_candle_data(symbol)
    
    def get_historical_data(self, symbol, resolution=None , days=None):
        """Return historical candle data for a symbol over the requested range."""
        return self.broker.get_historical_data(symbol, resolution, days)


if __name__ == "__main__":
    market_data = MarketData()
    #print(market_data.get_quotes("WIPRO"))
    print(market_data.get_candle_data("WIPRO"))
    # print(market_data.get_quotes("RELIANCE")['d'][0]['v'].get('lp'))
    # print(market_data.get_ltp("WIPRO"))
    # print(market_data.get_ltp("RELIANCE"))
    #print(market_data.get_bid_ask("WIPRO"))
    #print(market_data.get_bid_ask("RELIANCE"))
    #print(market_data.get_historical_data("WIPRO", resolution="D", days=20))
