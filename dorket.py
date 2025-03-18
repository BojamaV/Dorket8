from serpapi import GoogleSearch

params = {
  "q": search_query,
  "hl": "en",
  "gl": "us",
  "api_key": "your-serpapi-key"
}

search = GoogleSearch(params)
results = search.get_dict()
for result in results['organic_results']:
    print(result['link'])
