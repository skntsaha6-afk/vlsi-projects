'''This module will handle Fyers API client operations.

Examples:
	•	Get profile information
	•	Get funds information
	•	Get holdings information
	•	Place orders
	•	Get order book
	•	Get positions
	•	Get quotes
	•	Get historical data
    '''

import datetime
from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv
from auth.token_reader import get_token
from utils.normalize_symbol import normalize_symbol

load_dotenv()
CLIENT_ID = os.getenv("FYERS_CLIENT_ID")

class FyersClient:
    def __init__(self):
        """Initialize the Fyers client using the stored access token."""
        self.token = get_token()
        self.fyers = fyersModel.FyersModel(
            client_id=CLIENT_ID,
            is_async=False,
            token=self.token,
            log_path=""
        )

    def get_profile(self):
        """Return the authenticated user's profile details."""
        return self.fyers.get_profile()
    
    def get_funds(self):
        """Return the available funds and margin information."""
        return self.fyers.funds()
    
    def get_holdings(self):
        """Return the current holdings for the account."""
        return self.fyers.holdings()
    
    def place_order(self, order_data):
        """Place an order using the provided broker payload."""
        return self.fyers.place_order(order_data)   
    
    def get_order_book(self):
        """Return the current order book for the account."""
        return self.fyers.orderbook()
    
    def get_positions(self):
        """Return the open positions for the account."""
        return self.fyers.positions()

    def get_quotes(self, symbol):
        """Return the live quote response for one or more symbols."""

        data = {
                'symbols': symbol
        }
        return self.fyers.quotes(data=data) # Example: "symbols":"NSE:SBIN-EQ,NSE:IDEA-EQ"

    def get_history(self, history_data):
        """Return historical market data for the supplied request payload."""
        return self.fyers.history(data=history_data)

    def cancel_order(self, order_id):
        """Cancel an existing order by its broker order ID."""
        data = {
            "id": order_id
        }
        return self.fyers.cancel_order(data=data)
    
    def get_historical_data(self, symbol, resolution=None , days=None):
        """Return historical candle data for a symbol over the requested period."""
        symbol = normalize_symbol(symbol)
        if resolution is None:
            raise ValueError("resolution is required for historical data")
        if days is None or days <= 0:
            raise ValueError("days must be a positive integer")

        from_date = (datetime.date.today() - datetime.timedelta(days=days)).strftime("%Y-%m-%d")
        to_date = datetime.date.today().strftime("%Y-%m-%d")

        data = {
                "symbol": symbol,
                "resolution": resolution,
                "date_format": "1",
                "range_from":from_date,
                "range_to":to_date,
                "cont_flag":"1"
                }
        return self.fyers.history(data=data)

    def get_candle_data(self, symbol):
        """Return an OHLCV snapshot built from the latest quote response."""
        data = self.get_quotes(normalize_symbol(symbol))
        #print("Raw quote data:", data)  # Debugging statement to check the structure of the data
        quote_items = data.get("d", [])
        if not quote_items:
            #print("No quote items found for symbol:", symbol)  # Debugging statement
            return {}
        quote_values = quote_items[0].get("v", {})
        return {
            "open" : quote_values.get("open_price"),
            "high" : quote_values.get("high_price"),
            "low" : quote_values.get("low_price"),
            "close" : quote_values.get("lp"),
            "volume" : quote_values.get("volume"),
        } 
    
########### Commented out test code for demonstration purposes ############
if __name__ == "__main__":
    fyers= FyersClient()
#     print('Fyers Client initialized successfully!')
#     print('Fetching profile and funds information...')
#     print(fyers.get_profile()['data']['name'])
#     #print(fyers.get_funds())
#     print(fyers.get_holdings())
#     #print(fyers.get_positions())
#     #print(fyers.order_cancel(order_id="1234567890"))  # Replace with a valid order ID
#     print(fyers.get_quotes(symbol="NSE:RELIANCE-EQ"))
    #print(fyers.get_historical_data(symbol="WIPRO", resolution="D", days=20))
    #print(fyers.get_candle_data(symbol="WIPRO"))
