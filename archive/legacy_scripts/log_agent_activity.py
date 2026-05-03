import json
import datetime
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# WORKING CREDENTIALS
CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'
SPREADSHEET_ID = '1koC4XW64CBOoHgPSJM7DsRBNnbTPvgMDpbUNamWbGDY'
LOG_SHEET_NAME = '🚀 Agent Activity Log'

def log_activity(action_type, description, status="Completed"):
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
        
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # Row format: Timestamp, Agent, Action Type, Description, Status
        row_values = [[timestamp, 'Default Agent', action_type, description, status]]
        
        # Append to the bottom of the log sheet
        body = {
            'values': row_values
        }
        
        service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=f"'{LOG_SHEET_NAME}'!A1",
            valueInputOption="RAW",
            body=body
        ).execute()
        
        print(f"✅ Activity logged: {action_type} - {description}")
        return True
    except Exception as e:
        print(f"❌ Failed to log activity: {e}")
        return False

if __name__ == "__main__":
    # Test log for the "Wake up process" fix
    log_activity("System Fix", "Restored Agent Activity Log automated reporting via OAuth2", "Success")
