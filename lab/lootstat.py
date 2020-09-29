import json
import requests
from textwrap import indent

apiKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3M2U0MTExMC1iNzVmLTAxMzctMGRlZS03ZjI1NmUzMjk2MWIiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTY4Mjc0NDMxLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6InRvbWFzLW0tcGVyc3NvIn0.92JDktvNaTWGl4tRgXVDD-Xpp88HDlmtG5GKQ4j9sLI"

class pubgApi:
    baseUrl = "https://api.pubg.com/shards/"

    def __init__(self, apiKey):
        self.s = requests.Session()
        self.s.headers.update({"Authorization": "Bearer " + api_key})
        self.s.headers.update({"Accept": "application/vnd.api+json"})
        self.shards = "xbox"

    def query(self, endpoint):
        pass

class pubgPlayer:
    def __init__(self, name):
        self.name = name
        self.recent_matches = []

    def getRecentMatches(self, number):
        pass