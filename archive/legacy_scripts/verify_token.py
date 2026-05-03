import requests
import json

TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'

def verify_token():
    try:
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
        
        refresh_token = tokens.get('refresh_token')
        access_token = tokens.get('access_token')

        print(f"Checking token from {TOKEN_FILE}...")
        print(f"Refresh Token found: {refresh_token[:10]}...")

        # Check if the current access_token is still valid
        url = f"https://oauth2.googleapis.com/tokeninfo?access_token={access_token}"
        
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Access Token is still valid!")
            print(json.dumps(response.json(), indent=2))
        else:
            print("❌ Access Token expired or invalid.")
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
            print("\nNote: Current access token is expired. A refresh flow using the refresh_token is required.")
            print("This will require client_id and client_secret.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    verify_token()
