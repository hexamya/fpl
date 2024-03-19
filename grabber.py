import requests
import json
import time

session = requests.session()

seasons = session.get("https://www.fantasynutmeg.com/api/history/season").json()
with open(f"data/raw/seasons.json", "w", encoding="utf-8") as fp:
    json.dump(seasons, fp, ensure_ascii=False, indent=4)

index = 0
seasons_data = []
for index, season in enumerate(seasons):
    try:
        season_data = session.get(f"https://www.fantasynutmeg.com/api/history/season/{season}").json()["history"]
        season_data = list(map(lambda i: {"season": season} | i, season_data))
        seasons_data += season_data
    except Exception as err:
        print(err)

with open(f"data/raw/seasons_data.json", "w+", encoding="utf-8") as fp:
    json.dump(seasons_data, fp, ensure_ascii=False, indent=4)


players = session.get("https://www.fantasynutmeg.com/api/history/player/").json()
with open(f"data/raw/players.json", "w", encoding="utf-8") as fp:
    json.dump(players, fp, ensure_ascii=False, indent=4)


index = 0
players_data = []
for index, player in enumerate(players):
    try:
        player_data = session.get(f"https://www.fantasynutmeg.com/api/history/player/{player}").json()
        player_data = list(map(lambda i: {"player": index, "player_name": player} | i, player_data))
        players_data += player_data
    except Exception as err:
        print(err)

with open(f"data/raw/players_data.json", "w", encoding="utf-8") as fp:
    json.dump(players_data, fp, ensure_ascii=False, indent=4)