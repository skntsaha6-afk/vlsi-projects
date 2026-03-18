from datetime import datetime

def get_token():
    try:
        with open(f"auth/access_token.txt", "r") as f:
            access_token = f.read().strip()
            #print("Access Token read from file:", access_token)
    except FileNotFoundError:
        print("Access token file not found.")
        access_token = None
    return access_token