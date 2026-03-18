# from fyers_apiv3 import fyersModel
# import os
# from dotenv import load_dotenv
# from auth.token_reader import get_token 
# #auth.token_reader is the correct path to import get_token function from token_reader.py 
# # file inside auth directory
# #from token_reader import get_token
# from auth.generate_auth_code import generate_auth_code

# load_dotenv()
# #step 1: start flask server to capture auth code
# input("Press Enter to start the Flask server for authentication...")
# #step 2: generate auth code and open login URL
# generate_auth_code()

# #step 3: read access token from file and start trading bot
# CLIENT_ID = os.getenv("FYERS_CLIENT_ID")

# token = get_token()
# #print("Access Token:", token)

# fyers = fyersModel.FyersModel(
#         client_id= CLIENT_ID, 
#         is_async=False,
#         token=token,
#         log_path=""
#         )

# print('Fyers Trading bot started successfully!')
# print('Fetching profile and funds information...')
# print(fyers.get_profile())
# print(fyers.quotes(symbol="NSE:RELIANCE-EQ"))

from data.market_data import MarketData
from execution.order_manager import OrderManager
from strategies.moving_average_strategy import MovingAverageStrategy
from agents.trading_agent import TradingAgent
import time
from config.setting import PAPER_TRADING
from risk_management.risk_manager import RiskManager


market_data = MarketData()
risk_manager = RiskManager(max_trade_per_day=5, risk_per_trade=0.01, max_daily_loss=0.03)

order_manager = OrderManager(
        paper_trading = PAPER_TRADING
)

strategy = MovingAverageStrategy(market_data, order_manager)

agent = TradingAgent(strategy, risk_manager)

while True:
    print(agent.trade("RELIANCE"))
    time.sleep(300)