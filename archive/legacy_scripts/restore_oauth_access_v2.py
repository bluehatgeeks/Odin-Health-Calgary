import json
import os
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Try the second client secret found in keychain
CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET', '')
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'

def refresh_access_token():
    print(f"Attempting to refresh access token using keychain-derived secret: {CLIENT_SECRET}")
    try:
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
        
        refresh_token = tokens.get('refresh_token')
        if not refresh_token:
            print("❌ No refresh token found in token file.")
            return None

        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        }
        
        response = requests.post(token_url, data=data)
        if response.status_code != 200:
            print(f"❌ Refresh failed with status {response.status_code}: {response.text}")
            return None
            
        new_tokens = response.json()
        
        tokens['access_token'] = new_tokens['access_token']
        tokens['expires_in'] = new_tokens['expires_in']
        
        with open(TOKEN_FILE, 'w') as f:
            json.dump(tokens, f, indent=4)
            
        print("✅ Access token successfully refreshed and saved.")
        return new_tokens
    except Exception as e:
        print(f"❌ Error refreshing token: {e}")
        return None

def verify_sheets_access():
    try:
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
        
        creds = Credentials(
            token=tokens.get('access_token'),
            refresh_token=tokens.get('refresh_token'),
            token_uri="https://oauth2.googleapis.com/token",
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET
        )
        
        service = build('sheets', 'v4', credentials=creds)
        result = service.spreadsheets().list(pageSize=1).execute()
        print("✅ Google Sheets API access verified. Found spreadsheets:", result.get('values', []))
        return True
    except Exception as e:
        print(f"❌ Sheets API verification failed: {e}")
        return False

if __name__ == "__main__":
    if refresh_access_token():
        verify_sheets_access()
    else:
        print("Failed to refresh token, cannot verify access.")
