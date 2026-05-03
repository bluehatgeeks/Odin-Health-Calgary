import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# WORKING CREDENTIALS
CLIENT_ID = '637011530953-a80m8p8p3qaaj0mbur47fk3it3m2su9q.apps.googleusercontent.com'
CLIENT_SECRET = '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'
TOKEN_FILE = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary/.oauth_tokens.json'
PROJECT_ROOT = '/Users/alexandertretjakov/.copaw/workspaces/default/odin-calgary'

def get_drive_service():
    with open(TOKEN_FILE, 'r') as f:
        tokens = json.load(f)
    
    creds = Credentials(
        token=tokens.get('access_token'),
        refresh_token=tokens.get('refresh_token'),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    return build('drive', 'v3', credentials=creds)

def find_folder_by_name(service, name, parent_id=None):
    query = f"name = '{name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    if parent_id:
        query += f" and '{parent_id}' in parents"
    
    results = service.files().list(q=query, fields="files(id, name)").execute()
    items = results.get('files', [])
    return items[0]['id'] if items else None

def upload_file(service, local_path, drive_folder_id):
    file_name = os.path.basename(local_path)
    
    # Check if file already exists to avoid duplicates
    query = f"name = '{file_name}' and '{drive_folder_id}' in parents and trashed = false"
    results = service.files().list(q=query, fields="files(id)").execute()
    existing_files = results.get('files', [])
    
    file_metadata = {'name': file_name, 'parents': [drive_folder_id]}
    media = MediaFileUpload(local_path, mimetype='text/plain', resumable=True)
    
    if existing_files:
        file_id = existing_files[0]['id']
        print(f"Updating existing file: {file_name} (ID: {file_id})")
        updated_file = service.files().update(fileId=file_id, media_body=media).execute()
    else:
        print(f"Uploading new file: {file_name}")
        updated_file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        file_id = updated_file.get('id')
    
    return file_id

def sync_project():
    service = get_drive_service()
    
    # 1. Find or create the root project folder
    root_folder_name = "Odin Labs Clinic Operations"
    root_id = find_folder_by_name(service, root_folder_name)
    
    if not root_id:
        print(f"Creating root folder {root_folder_name}...")
        meta = {'name': root_folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
        root_id = service.files().create(body=meta, fields='id').execute().get('id')
    else:
        print(f"Found root folder: {root_folder_name} (ID: {root_id})")

    # 2. Walk through the local directory and sync
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Calculate relative path to maintain structure
        rel_path = os.path.relpath(root, PROJECT_ROOT)
        
        # Determine the drive folder to upload to
        if rel_path == ".":
            current_drive_folder = root_id
        else:
            # Ensure subdirectories exist on Drive
            path_parts = rel_path.split(os.sep)
            parent_id = root_id
            for part in path_parts:
                folder_id = find_folder_by_name(service, part, parent_id)
                if not folder_id:
                    print(f"Creating subfolder {part}...")
                    meta = {'name': part, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [parent_id]}
                    folder_id = service.files().create(body=meta, fields='id').execute().get('id')
                parent_id = folder_id
            current_drive_folder = parent_id

        for file in files:
            # Skip hidden files, token files, and the script itself
            if file.startswith('.') or file == 'restore_oauth_access.py' or 'verify' in file:
                continue
            
            local_path = os.path.join(root, file)
            try:
                upload_file(service, local_path, current_drive_folder)
            except Exception as e:
                print(f"❌ Failed to upload {file}: {e}")

if __name__ == "__main__":
    sync_project()
