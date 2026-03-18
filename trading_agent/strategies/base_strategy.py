class BaseStrategy:
    """Base strategy class, all strategies should follow this interface."""
    def __init__(self, market_data, order_manager):
        self.market_data = market_data
        self.order_manager = order_manager

    def generate_signal(self, symbol):
        """Generate trading signal based on market data.
        BUY
        SELL
        HOLD
        """
        raise NotImplementedError("Must implement generate_signal method in subclass.")
    
    def execute_trade(self, signal):
        """Execute trade based on generated signal."""
        raise NotImplementedError("Must implement execute_trade method in subclass.")


    