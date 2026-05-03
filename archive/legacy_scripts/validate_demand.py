import requests
import json

SERP_API_KEY = '498d84b71725bbb4b8409fc21622c37653024a66fe038a23f41761b3086aa0f4'
# Testing a mix of high-intent and problem-specific keywords to check volume/presence
KEYWORDS_TO_VALIDATE = [
    "Ayurveda Calgary",
    "Ayurvedic Doctor Calgary",
    "Panchkarma Treatment Calgary",
    "Holistic Gut Health Calgary",
    "Natural Inflammation Relief Calgary",
    "Ayurvedic Detox Calgary",
    "Integrative Medicine Calgary",
    "Holistic Health Clinic Calgary"
]

def validate_search_demand(keyword):
    print(f"Validating demand for: {keyword}...")
    params = {
        "q": keyword,
        "location": "Calgary,Alberta,Canada",
        "hl": "en",
        "gl": "ca",
        "api_key": SERP_API_KEY
    }
    
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        # We look for:
        # 1. Organic results count (if it's a real query, Google returns a full page)
        # 2. "Related searches" (indicates a cluster of interest)
        # 3. "People also ask" (shows specific intent patterns)
        
        organic = data.get('organic_results', [])
        related = data.get('related_searches', [])
        paa = data.get('related_questions', [])
        
        return {
            "keyword": keyword,
            "organic_count": len(organic),
            "has_related": len(related) > 0,
            "related_queries": [r.get('query') for r in related],
            "has_paa": len(paa) > 0,
            "paa_questions": [q.get('question') for q in paa]
        }
    except Exception as e:
        print(f"❌ Error validating {keyword}: {e}")
        return None

def main():
    results = []
    for kw in KEYWORDS_TO_VALIDATE:
        res = validate_search_demand(kw)
        if res:
            results.append(res)
            
    with open('odin-calgary/tech/keyword_demand_validation.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    print("\n✅ Demand validation complete. Data saved to odin-calgary/tech/keyword_demand_validation.json")

if __name__ == "__main__":
    main()
