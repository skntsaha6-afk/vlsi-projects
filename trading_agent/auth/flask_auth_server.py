import os
from flask import Flask, request
from dotenv import load_dotenv
from fyers_apiv3 import fyersModel
from datetime import datetime

'''
1. Start Flask server
      ↓
2. Generate login URL
      ↓
3. Login to FYERS
      ↓
4. Redirect → localhost:5000
      ↓
5. Flask captures auth_code
      ↓
6. Convert to access_token
      ↓
7. Save access_token.txt
      ↓
8. Trading bot reads token
'''

load_dotenv()

CLIENT_ID = os.getenv("FYERS_CLIENT_ID")
SECRET_KEY = os.getenv("FYERS_SECRET_KEY")
REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI")
GRANT_TYPE = os.getenv("FYERS_GRANT_TYPE")
RESPONSE_TYPE = os.getenv("FYERS_RESPONSE_TYPE")

app = Flask(__name__)

@app.route("/")
def capture_auth():

    auth_code = request.args.get("auth_code")

    if not auth_code:
        return "Auth code missing"

    session = fyersModel.SessionModel(
        client_id=CLIENT_ID,
        secret_key=SECRET_KEY,
        redirect_uri=REDIRECT_URI,
        response_type=RESPONSE_TYPE,
        grant_type=GRANT_TYPE
    )

    session.set_token(auth_code)

    response = session.generate_token()

    access_token = response["access_token"]

    with open(f"auth/access_token.txt", "w") as f:
        f.write(access_token)

    return "Login successful. Token saved."

if __name__ == "__main__":
    app.run(port=5000)