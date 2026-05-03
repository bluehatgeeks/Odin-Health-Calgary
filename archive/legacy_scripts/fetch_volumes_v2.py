import requests
import json

# Configuration
KE_API_KEY = 'f9072c25433b741507b4'
COUNTRY = 'ca'  # Canada
CURRENCY = 'usd'
DATA_SOURCE = 'cli' # Google Keyword Planner & Clickstream data

KEYWORDS_TO_VALIDATE = [
    "Ayurveda Calgary",
    "Ayurvedic Doctor Calgary",
    "Panchkarma Treatment Calgary",
    "Holistic Gut Health Calgary",
    "Natural Inflammation Relief Calgary",
    "Ayurvedic Detox Calgary",
    "Integrative Medicine Calgary",
    "Holistic Health Clinic Calgary",
    "Naturopath Calgary",
    "Functional Medicine Calgary"
]

def get_keyword_volumes():
    print(f"Requesting volumes for {len(KEYWORDS_TO_VALIDATE)} keywords...")
    url = "https://api.keywordseverywhere.com/v1/get_keyword_data"
    
    headers = {
        "Authorization": f"Bearer {KE_API_KEY}",
        "Accept": "application/json",
        "Content-type": "application/json"
    }
    
    payload = {
        "kw": KEYWORDS_TO_VALIDATE,
        "country": COUNTRY,
        "currency": CURRENCY,
        "dataSource": DATA_SOURCE
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data:
            results = []
            for item in data['data']:
                results.append({
                    "keyword": item.get('keyword'),
                    "monthly_volume": item.get('vol'),
                    "cpc": item.get('cpc', {}).get('value', 'N/A'),
                    "competition": item.get('competition')
                })
            return results
        else:
            print(f"⚠️ Unexpected API response format: {data}")
            return None
            
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

def main():
    volume_matrix = get_keyword_volumes()
    if volume_matrix:
        with open('odin-calgary/tech/keyword_volume_matrix.json', 'w') as f:
            json.dump(volume_matrix, f, indent=4)
        print("\n✅ Quantitative Volume Matrix successfully created.")
        print("Data saved to odin-calgary/tech/keyword_volume_matrix.json")
    else:
        print("\n❌ Failed to retrieve volume data.")

if __name__ == "__main__":
    main()
