import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

FYERS_LOGIN_URL = os.getenv("FYERS_LOGIN_URL")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(FYERS_LOGIN_URL)

input("Login in browser then press Enter...")

current_url = driver.current_url

auth_code = current_url.split("auth_code=")[1].split("&")[0]

with open("auth/auth_code.txt", "w") as f:
    f.write(auth_code)

print("Auth code captured:", auth_code)

driver.quit()