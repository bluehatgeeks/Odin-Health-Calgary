import requests
import json

# Configuration
KE_API_KEY = 'f9072c25433b741507b4'
# We are targeting Calgary, Alberta, Canada
LOCATION = 'Calgary, Alberta, Canada'

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

def get_keyword_volume(keyword):
    print(f"Fetching volume for: {keyword}...")
    # Keywords Everywhere API endpoint for keyword volume
    url = f"https://api.keywordseverywhere.com/v1/get_keyword_volume"
    params = {
        "key": KE_API_KEY,
        "keyword": keyword,
        "location": LOCATION
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        # Keywords Everywhere returns data in a specific format
        # We want the 'vol' (volume) and 'cpc' (cost per click)
        if data.get('status') == 'success' or 'data' in data:
            stats = data.get('data', [{}])[0]
            return {
                "keyword": keyword,
                "monthly_volume": stats.get('vol', 0),
                "cpc": stats.get('cpc', 'N/A'),
                "competition": stats.get('competition', 'N/A')
            }
        else:
            print(f"⚠️ API returned non-success for {keyword}: {data}")
            return None
            
    except Exception as e:
        print(f"❌ Error fetching {keyword}: {e}")
        return None

def main():
    volume_matrix = []
    for kw in KEYWORDS_TO_VALIDATE:
        res = get_keyword_volume(kw)
        if res:
            volume_matrix.append(res)
    
    # Save the quantitative data
    with open('odin-calgary/tech/keyword_volume_matrix.json', 'w') as f:
        json.dump(volume_matrix, f, indent=4)
    
    print("\n✅ Quantitative Volume Matrix successfully created.")
    print("Data saved to odin-calgary/tech/keyword_volume_matrix.json")

if __name__ == "__main__":
    main()
