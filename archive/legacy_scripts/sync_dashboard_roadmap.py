import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'
SPREADSHEET_ID = '1koC4XW64CBOoHgPSJM7DsRBNnbTPvgMDpbUNamWbGDY'

def update_dashboard_status():
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
        
        # Target the "Roadmap" sheet
        target_sheet = "Roadmap"
        
        # Based on debug_roadmap.py:
        # Row 4: 'Finalize GHL -> Sheets -> Drive Pipeline' -> Status is Column E (Index 4)
        # We are updating Row 4, Column E to 'Completed'
        # And we can add a note about the Drive Sync and OAuth2 restoration
        
        updates = [
            {
                'range': f"'{target_sheet}'!E4", 
                'values': [['Completed']]
            },
            {
                'range': f"'{target_sheet}'!H4", 
                'values': [['Verified: OAuth2 restored & Autonomous Drive Sync implemented']]
            }
        ]
        
        body = {'valueInputOption': 'RAW', 'data': updates}
        service.spreadsheets().values().batchUpdate(spreadsheetId=SPREADSHEET_ID, body=body).execute()
        print("✅ Dashboard roadmap updated: Pipeline marked as 'Completed' and notes added.")

    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")

if __name__ == "__main__":
    update_dashboard_status()
