from strategies.base_strategy import BaseStrategy
import pandas as pd

class MovingAverageStrategy(BaseStrategy):

    def generate_signal(self, symbol):
        candles = self.market_data.get_historical_data(
                        symbol, 
                        resolution="D" , 
                        days=100
                    )  
        df = pd.DataFrame(
                    candles["candles"],
                    columns=["time", "open", "high", "low", "close", "volume"]
        )
    
        df["MA20"] = df["close"].rolling(20).mean()
        df["MA50"] = df["close"].rolling(50).mean()

        latest = df.iloc[-1]

        if latest["MA20"] > latest["MA50"]:
            return "BUY"

        if latest["MA20"] < latest["MA50"]:
            return "SELL"

        return "HOLD"
    
