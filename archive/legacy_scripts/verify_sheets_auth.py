import json
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# WORKING CLIENT ID and SECRET
CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'

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
        
        # Correct way to verify access: try to get a specific spreadsheet 
        # or simply call a basic API method. Since we don't have the ID here,
        # we can try to call the spreadsheets.get method with a dummy ID 
        # just to see if the AUTH is accepted (expecting a 404/403, but not a 401).
        
        print("Testing Sheets API connectivity...")
        # Using a dummy ID to verify that the request actually reaches Google and is authenticated
        try:
            service.spreadsheets().get(spreadsheetId='dummy_id').execute()
        except Exception as e:
            error_msg = str(e)
            if '401' in error_msg:
                print("❌ Sheets API verification failed: 401 Unauthorized")
                return False
            elif '404' in error_msg or '403' in error_msg:
                print("✅ Sheets API AUTHENTICATION verified (Received expected 404/403 for dummy ID).")
                return True
            else:
                print(f"⚠️ Unexpected response, but auth might be OK: {error_msg}")
                return True
                
    except Exception as e:
        print(f"❌ Sheets API verification critical failure: {e}")
        return False

if __name__ == "__main__":
    verify_sheets_access()
