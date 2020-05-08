import json
import requests
from textwrap import indent

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3M2U0MTExMC1iNzVmLTAxMzctMGRlZS03ZjI1NmUzMjk2MWIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTY4Mjc0NDMxLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InRvbWFzLW0tcGVyc3NvIn0.92JDktvNaTWGl4tRgXVDD-Xpp88HDlmtG5GKQ4j9sLI"

url = "https://api.pubg.com/shards/xbox/players?filter[playerNames]=MutX"

header = {
  "Authorization": "Bearer " + api_key,
  "Accept": "application/vnd.api+json"
}

r = requests.get(url, headers=header)
print(r.json())
print(json.dumps(r.json(), indent=2))

player = r.json()

print(player["data"][0]["id"])