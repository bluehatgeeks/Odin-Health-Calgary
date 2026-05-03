#!/usr/bin/env python3
"""Reliable file-by-file sync with progress."""

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path
import time

PROJECT_ROOT = Path('/Users/alexandertretjakov/Downloads/odin-labs-calgary')
TOKEN_PATH = Path.home() / '.hermes/google_token.json'
PARENT_ID = '1i0J2ICnGAbcPAqiFSS1RFyMT10kfSLjO'

def get_or_create_folder(service, parent_id, folder_name):
    """Get or create a folder, return ID."""
    query = f"mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents and name='{folder_name}' and trashed=false"
    results = service.files().list(q=query, fields='files(id, name)').execute()
    items = results.get('files', [])
    
    if items:
        return items[0]['id']
    
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=file_metadata, fields='id').execute()
    return folder['id']

def upload_file(service, file_path, parent_id):
    """Upload a single file."""
    try:
        file_metadata = {'name': file_path.name, 'parents': [parent_id]}
        media = MediaFileUpload(str(file_path), mimetype='text/markdown' if file_path.suffix == '.md' else 'application/json', resumable=True)
        result = service.files().create(body=file_metadata, media_body=media, fields='id, name').execute()
        return True, result['name']
    except Exception as e:
        return False, str(e)

def main():
    print("═" * 70)
    print("Odin Labs Calgary - Google Drive Sync")
    print("═" * 70)
    
    creds = Credentials.from_authorized_user_file(str(TOKEN_PATH))
    service = build('drive', 'v3', credentials=creds)
    
    # Folder structure to sync
    folders_to_sync = [
        ('00_ADMIN', None),
        ('01_BUSINESS_STRATEGY', None),
        ('02_MARKET_INTEL', None),
        ('03_CLINICAL_OPERATIONS', ['protocols', 'consumables']),
        ('04_PATIENT_EXPERIENCE', None),
        ('05_STAFFING', None),
        ('06_MARKETING_GROWTH', ['google_ads']),
        ('07_TECH_STACK', ['integrations', 'keyword_data']),
        ('08_OPERATIONS_PLAYBOOK', None),
        ('09_MEETINGS_LOGS', None),
        ('archive', ['legacy_scripts']),
    ]
    
    total_uploaded = 0
    start_time = time.time()
    
    for folder_name, subfolders in folders_to_sync:
        local_path = PROJECT_ROOT / folder_name
        if not local_path.exists():
            continue
        
        print(f"\n📂 {folder_name}")
        drive_folder_id = get_or_create_folder(service, PARENT_ID, folder_name)
        
        if subfolders:
            # Handle subfolders
            for sub in subfolders:
                sub_path = local_path / sub
                if not sub_path.exists():
                    continue
                
                print(f"  └─ {sub}/")
                sub_folder_id = get_or_create_folder(service, drive_folder_id, sub)
                
                # Upload files in subfolder
                for file in list(sub_path.glob('*.md')) + list(sub_path.glob('*.json')):
                    success, msg = upload_file(service, file, sub_folder_id)
                    if success:
                        print(f"      ✓ {file.name}")
                        total_uploaded += 1
                    else:
                        print(f"      ✗ {file.name}: {msg}")
        else:
            # Direct files
            for file in list(local_path.glob('*.md')) + list(local_path.glob('*.json')):
                success, msg = upload_file(service, file, drive_folder_id)
                if success:
                    print(f"  ✓ {file.name}")
                    total_uploaded += 1
                else:
                    print(f"  ✗ {file.name}: {msg}")
    
    # Upload README
    print(f"\n📄 README.md")
    success, msg = upload_file(service, PROJECT_ROOT / 'README.md', PARENT_ID)
    if success:
        print(f"  ✓ README.md")
        total_uploaded += 1
    
    elapsed = time.time() - start_time
    print("\n" + "═" * 70)
    print(f"✓ Sync complete: {total_uploaded} files in {elapsed:.1f}s")
    print(f"  Drive: https://drive.google.com/drive/folders/{PARENT_ID}")
    print("═" * 70)

if __name__ == '__main__':
    main()
