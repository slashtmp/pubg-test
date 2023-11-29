import config
import pubg

q = pubg.API(config.shard, config.apiKey)

res1 = q.players(playerNames=["MutX", "SnowyGnome", "Xeraor77"])
for pl in res1:
    q.type(pl)

res2 = q.seasons()

p = pubg.objects.Player("MutX")

print(res2)