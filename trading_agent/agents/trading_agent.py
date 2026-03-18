class TradingAgent:
    def __init__(self, strategy, risk_manager):
        self.strategy = strategy
        self.risk_manager = risk_manager
    
    def trade(self, symbol):
        signal = self.strategy.generate_signal(symbol)

        is_allowed, message = self.risk_manager.can_trade(signal)
        if not is_allowed:
            print(f"Trade not allowed: {message}")
            return "BLOCKED"
        price = self.strategy.market_data.get_ltp(symbol)
        qty = self.risk_manager.position_sizing(price)

        if signal == "BUY":
            return self.strategy.order_manager.buy(symbol, qty=qty)

        if signal == "SELL":
            return self.strategy.order_manager.sell(symbol, qty=qty)
        
            return "HOLD"
        
        self.risk_manager.update_trade(signal)

        return f"Executed {signal} for {symbol} at price {price} with quantity {qty}"

