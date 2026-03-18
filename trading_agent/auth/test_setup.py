import pandas, requests, fyers_apiv3
from dotenv import load_dotenv
import os
load_dotenv()
print(os.getenv("FYERS_ID"))
print("Setting up test environment...")