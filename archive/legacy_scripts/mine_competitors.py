import requests
import json

# Configuration
SERP_API_KEY = '498d84b71725bbb4b8409fc21622c37653024a66fe038a23f41761b3086aa0f4'
SEARCH_QUERIES = [
    "ayurveda clinic calgary",
    "holistic health calgary",
    "ayurvedic treatment calgary",
    "best holistic wellness calgary"
]

def mine_competitor_ads(query):
    print(f"Mining ads for: {query}...")
    params = {
        "q": query,
        "location": "Calgary,Alberta,Canada",
        "hl": "en",
        "gl": "ca",
        "api_key": SERP_API_KEY
    }
    
    try:
        response = requests.get("https://serpapi.com/search", params=params)
        response.raise_for_status()
        data = response.json()
        
        # Extract Ad results
        ads = data.get('ads', [])
        organic = data.get('organic_results', [])
        
        return {
            "query": query,
            "ads": ads,
            "organic": organic[:5] # Top 5 organic for keyword intent
        }
    except Exception as e:
        print(f"❌ Error mining {query}: {e}")
        return None

def main():
    all_data = []
    for q in SEARCH_QUERIES:
        result = mine_competitor_ads(q)
        if result:
            all_data.append(result)
    
    # Save results for analysis
    with open('odin-calgary/tech/serp_market_data.json', 'w') as f:
        json.dump(all_data, f, indent=4)
    
    print("\n✅ Market data successfully mined to odin-calgary/tech/serp_market_data.json")

if __name__ == "__main__":
    main()
