#import pubg.api
from . import api

class Player:
    
    def __init__(self, playerName=None) -> None:
        #self.playerName = playerName
        #self.playerId = playerId
        pass

    def load(self, playerName):
        #api = api.API()
        a = api.API()
        res = a.players(playerNames=playerName)
        print(res)

        

class Match:
    pass

class Season:
    pass