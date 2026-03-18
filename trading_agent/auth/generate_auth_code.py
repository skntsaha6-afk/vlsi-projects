import os
from dotenv import load_dotenv
from fyers_apiv3 import fyersModel
import webbrowser

def generate_auth_code():
    load_dotenv(override=True)

    try : 
        CLIENT_ID = os.getenv("FYERS_CLIENT_ID")
        SECRET_KEY = os.getenv("FYERS_SECRET_KEY")
        REDIRECT_URI = os.getenv("FYERS_REDIRECT_URI")
        RESPONSE_TYPE = os.getenv("FYERS_RESPONSE_TYPE")
        GRANT_TYPE = os.getenv("FYERS_GRANT_TYPE")

        session = fyersModel.SessionModel(
            client_id=CLIENT_ID,
            secret_key=SECRET_KEY,
            redirect_uri=REDIRECT_URI,
            response_type=RESPONSE_TYPE,
            grant_type=GRANT_TYPE
        )

        login_url = session.generate_authcode()

        print("Open this URL in browser:")
        print(login_url)
        webbrowser.open(login_url,new=2)

    except Exception as e:
        print("Error generating auth code:", str(e))
    
if __name__ == "__main__":
    generate_auth_code()