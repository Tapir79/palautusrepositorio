import requests
from player import Player

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    NAME = 4

def sort_by_key(player, sort_by):
    match sort_by:
        case SortBy.POINTS:
            return player.points
        case SortBy.GOALS:
            return player.goals
        case SortBy.ASSISTS:
                return player.assists
        case SortBy.NAME:
                return player.name
        case _:
            raise ValueError(f"Unknown SortBy value: {sort_by}")

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    sort_by = SortBy.POINTS

    finnish_players = [player for player in players if player.nationality == "FIN"]
    sorted_finnish_players = sorted(
         finnish_players, 
         reverse=True,
         key=lambda player: sort_by_key(player, sort_by))

    print("Players from FIN")
    for player in sorted_finnish_players:
        print(player)

if __name__ == "__main__":
    main()
