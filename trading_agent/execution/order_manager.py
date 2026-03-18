from execution.fyers_client import FyersClient
from utils.normalize_symbol import normalize_symbol

class OrderManager:

    def __init__(self,broker=None, paper_trading=False):
        """Initialize the order manager with an optional broker client."""
        self.broker = broker if broker else FyersClient()
        self.paper_trading = paper_trading

    # BUY ORDER
    def buy(self, symbol, qty, price=None, orderType = None , sl = None, tp = None, offlineOrder = False, **kwargs):
        """Place a buy order for the given symbol and quantity."""
        order_data = {      
            "symbol": normalize_symbol(symbol),
            "qty":qty,
            "type":orderType if orderType else 2, # Default to Market Order
            "side":1,
            "productType":"INTRADAY",
            "limitPrice":price if price else 0,
            "stopPrice":0,
            "validity":"DAY",
            "disclosedQty":0,
            "offlineOrder":False,
            "orderTag":"tag1",
            "isSliceOrder":False,
            "stopLoss":sl if sl else 0,
            "takeProfit":tp if tp else 0,
            "offlineOrder":offlineOrder
        }

        if self.paper_trading:
            print(f"Paper Trading Mode: Simulated BUY order for {qty} shares of {symbol} at price {price if price else 'Market Price'}")
            return {"status": "success", "message": "Simulated BUY order placed successfully."}
        return self.broker.place_order(order_data)
    
    # SELL ORDER
    def sell(self, symbol, qty, price=None, orderType = None , sl = None, tp = None, offlineOrder = False, **kwargs):
        """Place a sell order for the given symbol and quantity."""
        order_data = {      
            "symbol": normalize_symbol(symbol),
            "qty":qty,
            "type":orderType if orderType else 2, # Default to Market Order
            "side":-1, # Sell order -1
            "productType":"INTRADAY",
            "limitPrice":price if price else 0,
            "stopPrice":0,
            "validity":"DAY",
            "disclosedQty":0,
            "orderTag":"tag1",
            "isSliceOrder":False,
            "stopLoss":sl if sl else 0,
            "takeProfit":tp if tp else 0,
            "offlineOrder":offlineOrder
        }
        if self.paper_trading:
            print(f"Paper Trading Mode: Simulated SELL order for {qty} shares of {symbol} at price {price if price else 'Market Price'}")
            return {"status": "success", "message": "Simulated SELL order placed successfully."}
        return self.broker.place_order(order_data)
    
    #get profile, cancel order, get order book, get positions, get funds, get quotes
    def get_profile(self):
        """Return the authenticated user's profile details."""
        return self.broker.get_profile()
    
    def cancel_order(self, order_id):
        """Cancel an order using its broker order ID."""
        return self.broker.cancel_order(order_id)
    
    def get_order_book(self):
        """Return the current order book."""
        return self.broker.get_order_book()
    
    def get_positions(self):
        """Return the current open positions."""
        return self.broker.get_positions()
    
    def get_funds(self):
        """Return funds and margin information."""
        return self.broker.get_funds()
    
    def get_quotes(self, symbol):
        """Return the latest quote response for the given symbol."""
        symbol =  normalize_symbol(symbol)
        return self.broker.get_quotes(symbol)
    
# if __name__ == "__main__":
#     broker = FyersClient()
#     order_manager = OrderManager(broker)
#     print('Order Manager initialized successfully!')
#     print('Fetching profile and funds information...')
#     print(order_manager.get_profile()['data']['name'])
#     print(order_manager.get_funds())
#     print(order_manager.get_positions())
# #     # Example of placing a buy order
#     response_buy = order_manager.buy(symbol="RELIANCE", qty=1, offlineOrder=False)  # Market Order
#      #response_sell = order_manager.sell(symbol="RELIANCE", qty=1)  # Market Order
#     print(response_buy)
# #    print(response_sell)
#     #print(order_manager.get_quotes("WIPRO"))  # Fetch quotes for WIPRO
#     #print(order_manager.cancel_order(order_id=response_buy['id']))  # Cancel the buy order using the returned order ID
#     #print(order_manager.get_order_book())  # Replace with a valid order ID
