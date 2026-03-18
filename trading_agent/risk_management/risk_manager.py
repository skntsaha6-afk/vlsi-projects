class RiskManager:

    def __init__(self, max_trade_per_day,risk_per_trade = 0.01, max_daily_loss = 0.03):
        """ risk : 1% and 
            max loss : 3% of total capital 
        """
        self.max_trade_per_day = max_trade_per_day
        self.risk_per_trade = risk_per_trade
        self.max_daily_loss = max_daily_loss

        self.trade_count= 0 
        self.daily_loss = 0
        self.last_signal = None

        # simulated capital for risk management
        self.capital = 50000

    def is_duplicate_signal(self, signal):
        return signal == self.last_signal
        
    def can_trade(self, signal):

        if signal not in ["BUY", "SELL"]:
            return False, "Invalid signal"
            
        if self.is_duplicate_signal(signal):
            return False, "Duplicate signal"
            
        if self.trade_count >= self.max_trade_per_day:
            return False, "Max trades per day reached"
            
        if self.daily_loss >= self.max_daily_loss * self.capital:
            return False, "Max daily loss reached"
            
        return True, "Trade allowed"
        
    def update_trade(self, signal):
        self.last_signal = signal
        self.trade_count +=1

        
    def position_sizing(self, price):
        risk_amount =  self.capital * self.risk_per_trade
        quantity = int(risk_amount / price)
        return max(quantity, 1)
        
    def update_pnl(self, pnl):
        self.daily_loss += pnl

    def reset_daily(self):
        self.trade_count = 0
        self.daily_loss = 0
        self.last_signal = None
        


        






