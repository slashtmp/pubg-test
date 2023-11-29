import requests
from requests.compat import urljoin
from functools import wraps
from urllib.parse import urlunsplit
from . import jsonapi

def endpoint(ep):
    """
    wrap an endpoint funcion with API url
    and manage the result in a proper way
    """
    def decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):

            # The decorated method constructs the query string
            query = method(self, *args, **kwargs)

            # In case of a generic endpoint, set query to an empty
            # dict for better error handling.
            if not query:
                query = {}

            try:
                path = f"{self.apiPath}{ep}/{query['path']}"
            except KeyError:
                path = self.apiPath + ep

            queryURL = urlunsplit((
                self.apiScheme,
                self.apiNetloc,
                path,
                query.get('queryString'),
                ""
            ))

            res = self.session.get(queryURL)
            if res.ok:
                return jsonapi.Document(res.json())
            else:
                raise ConnectionError(
                    f"Return Code: {res.reason}\n"
                    f"{res.json()['error']['title']}\n"
                    f"{res.json()['error']['detail']}\n"
                    )

        return wrapper
    return decorator

class API:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, shard=None, apiKey=None):
        if not hasattr(self, "session"):
            if not (shard and apiKey):
                raise TypeError("Initialisin an API session requires shard and apiKey")

            headers = {
                "Authorization": f"Bearer {apiKey}",
                "Accept": "application/vnd.api+json"
            } 
            self.session = requests.Session()
            self.session.headers.update(headers)
            self.apiScheme = "https"
            self.apiNetloc = "api.pubg.com"
            self.apiPath = f"/shards/{shard}/"
            self.baseURL = "https://api.pubg.com/"
            self.apiURL = urljoin(self.baseURL, "/".join(["shards", shard])) + "/"

    @staticmethod
    def type(obj) -> str:
        """Return type of PUBG object"""

        # Handles both request response and the json dict
        if(isinstance(obj, requests.models.Response)):
            res = obj.json()
        elif(isinstance(obj, dict)):
            res = obj
        else:
            raise TypeError("Argument must be a Request respons or dict.")

        #
        # Resources are expected to be in JSON:API format, so validate by
        # checking for 'type' and 'id'.
        #
        # If the input is a top-level object, the 'data' memeber should be
        # present and may be an array or a single resource object, so both
        # possibilities must be caterred for.
        #

        if 'data' in res:
            # data is an array, generate a set and ensure the types are unique
            if isinstance(res['data'], list):
                typeSet = { e['type'] for e in res['data'] }
                if len(typeSet) == 1:
                    resType = typeSet.pop()
                else:
                    raise TypeError("Multiple types in resource")
                    
            # data is not a list
            else:
                resType = res['data']['type']
        else:
            resType = res['type']

        return resType

    @endpoint("players")
    def player(self, playerId):
        """ Query a single PlayerId """
        return { "path": playerId }

    @endpoint("players")
    def players(self, playerIds=None, playerNames=None):
        if playerIds and playerNames:
            raise TypeError("Only one of playerIDs or playerNames must be specified")

        if playerIds:
            filter = "filter[playerIds]="
            playerList = playerIds
        elif playerNames:
            filter = "filter[playerNames]="
            playerList = playerNames
        else:
            raise TypeError("One of playerIDs or playerNames must be specified")

        #
        # If playerList is a string with comma separated players,
        # transorm it to a list of stings.
        #
        if isinstance(playerList, str):
            pl = playerList.split(",")
            playerList = [ p.strip() for p in pl ]

        return { "queryString" : filter + (",").join(playerList) }

    @endpoint("matches")
    def matches(self, matchId):
        return { "path": matchId }

    @endpoint("seasons")
    def seasons(self):
        pass

    @endpoint("players")
    def lifetime(self, playerId=None):
        return { "path": f"{playerId}/seasons/lifetime" }