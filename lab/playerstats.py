import json
import requests
from textwrap import indent

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3M2U0MTExMC1iNzVmLTAxMzctMGRlZS03ZjI1NmUzMjk2MWIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTY4Mjc0NDMxLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InRvbWFzLW0tcGVyc3NvIn0.92JDktvNaTWGl4tRgXVDD-Xpp88HDlmtG5GKQ4j9sLI"

#url = "https://api.pubg.com/shards/xbox/players?filter[playerNames]=MutX"

header = {
  "Authorization": "Bearer " + api_key,
  "Accept": "application/vnd.api+json"
}
urlBase = "https://api.pubg.com/shards/xbox/"
urlSeasonList = urlBase + "seasons"

r = requests.get(urlSeasonList, headers=header)

#print( json.dumps(r.json(), indent=2) )

seasons = r.json()
for i in seasons["data"]:
    if( i["attributes"]["isCurrentSeason"]):
        currentSeason =  i["id"]

playerName = "MutX"
urlPlayer = urlBase + "players?filter[playerNames]=" + playerName
r = requests.get(urlPlayer, headers=header)

matchList = r.json()["data"][0]["relationships"]["matches"]["data"]
for match in matchList[:1]:
        print( match["id"] )
        urlMatch = urlBase + "matches/" + match["id"]
        rMatch = requests.get(urlMatch, headers=header)
        xx = rMatch.json()
        for i in xx["included"]:
            if( i['type'] == "asset"):
                print( i['attributes']['URL'] )

        print( json.dumps(rMatch.json(), indent = 2 ) )