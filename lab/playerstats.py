import json
import requests
from textwrap import indent

telemetryUrl = []

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

playerName = "Rokku"
lootGround = 0
lootCarePackage = 0
lootDeathbox = 0
urlPlayer = urlBase + "players?filter[playerNames]=" + playerName
r = requests.get(urlPlayer, headers=header)

matchList = r.json()["data"][0]["relationships"]["matches"]["data"]
for match in matchList[:1]:
        print( match["id"] )
        urlMatch = urlBase + "matches/" + match["id"]
        rMatch = requests.get(urlMatch, headers=header)
        
        for i in rMatch.json()["included"]:
            if( i['type'] == "asset" and i['attributes']['URL'] ):
                telemetryUrl.append( i['attributes']['URL'] )

telemetryHeader = {
    "Accept": "application/vnd.api+json",
    "Accept-Encoding": "gzip"
}

for url in telemetryUrl:
    r = requests.get( url, telemetryHeader )
    telemetry = r.json()

    for row in telemetry:
        if( row['_T'] == "LogMatchDefinition" ):
            continue
        if( row['common']['isGame'] < 0.1 ):
            continue

        if( row['_T'] == "LogItemPickup" and row['character']['name'] == playerName):
            lootGround += 1
        if( row['_T'] == "LogItemPickupFromCarepackage" and row['character']['name'] == playerName):
            lootCarePackage += 1
        if( row['_T'] == "LogItemPickupFromLootBox" and row['character']['name'] == playerName):
            lootDeathbox += 1

print( "Ground loot:", lootGround)
print( "Carepackage loot:", lootCarePackage)
print( "Deathbox loot", lootDeathbox)