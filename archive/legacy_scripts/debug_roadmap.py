import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'
SPREADSHEET_ID = '1koC4XW64CBOoHgPSJM7DsRBNnbTPvgMDpbUNamWbGDY'

def debug_roadmap_content():
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
        
        # Read a larger range to see what's actually there
        range_name = "'Roadmap'!A1:Z100"
        result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=range_name).execute()
        values = result.get('values', [])
        
        print("--- CURRENT ROADMAP CONTENT ---")
        for i, row in enumerate(values):
            print(f"Row {i+1}: {row}")
        print("-------------------------------")
        
    except Exception as e:
        print(f"❌ Error reading dashboard: {e}")

if __name__ == "__main__":
    debug_roadmap_content()
