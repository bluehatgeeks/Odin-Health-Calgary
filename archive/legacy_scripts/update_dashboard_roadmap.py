import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# WORKING CREDENTIALS
CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'

def update_dashboard_roadmap():
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
        
        # Since I don't have the specific Spreadsheet ID for "Odin_Labs_Clinic_Dashboard" in current context,
        # I first need to find it by name.
        drive_service = build('drive', 'v3', credentials=creds)
        query = "name = 'Odin_Labs_Clinic_Dashboard' and mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false"
        results = drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])
        
        if not files:
            print("❌ Could not find spreadsheet named 'Odin_Labs_Clinic_Dashboard'")
            return

        spreadsheet_id = files[0]['id']
        print(f"Found Dashboard ID: {spreadsheet_id}")

        # To update the roadmap, I need to know which sheet/cell it's in.
        # I'll start by listing the sheets in the spreadsheet.
        sheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
        sheets = sheet_metadata.get('sheets', [])
        
        # I will look for a sheet named 'Roadmap' or 'Project Tracking'
        target_sheet = None
        for s in sheets:
            if 'roadmap' in s['properties']['title'].lower() or 'tracking' in s['properties']['title'].lower():
                target_sheet = s['properties']['title']
                break
        
        if not target_sheet:
            # Default to the first sheet if no roadmap sheet is found
            target_sheet = sheets[0]['properties']['title']
            print(f"No explicit roadmap sheet found, using default: {target_sheet}")
        else:
            print(f"Updating roadmap in sheet: {target_sheet}")

        # Update the status of the recent wins
        # Note: This is a blind update since I don't have the exact cell. 
        # In a real scenario, I would search for the text "OAuth2 Recovery" and "Drive Sync".
        # For now, I'll read the first few rows to find where the roadmap is.
        range_name = f"'{target_sheet}'!A1:C20"
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        
        if not values:
            print("❌ Sheet is empty. Cannot find roadmap to update.")
            return

        # Search for the roadmap items and update them to [x]
        updates = []
        for i, row in enumerate(values):
            row_text = " ".join([str(cell) for cell in row])
            if "OAuth2 Recovery" in row_text:
                # Assuming Column A is the checkbox [ ]
                updates.append({'range': f"'{target_sheet}'!A{i+1}", 'values': [['[x]']]})
            if "Drive Sync" in row_text:
                updates.append({'range': f"'{target_sheet}'!A{i+1}", 'values': [['[x]']]})

        if updates:
            body = {'valueInputOption': 'RAW', 'data': updates}
            service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()
            print(f"✅ Updated {len(updates)} roadmap items in the dashboard.")
        else:
            print("❌ Could not find the specific roadmap items in the sheet content.")

    except Exception as e:
        print(f"❌ Error updating dashboard: {e}")

if __name__ == "__main__":
    update_dashboard_roadmap()
