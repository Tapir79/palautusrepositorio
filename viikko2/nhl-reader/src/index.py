import requests
from player import Player

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    NAME = 4

def get_players_from_response(response):
    players = []
    for player_dict in response:
        player = Player(player_dict)
        players.append(player)
    return players


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
         
def filter_finnish_players(players):
    return [player for player in players if player.nationality == "FIN"]

def sorted_finnish_players(players, sort_by):
    finnish_players = filter_finnish_players(players)
    return sorted(
         finnish_players, 
         reverse=True,
         key=lambda player: sort_by_key(player, sort_by))

def print_players(players):
    print("Players from FIN")
    for player in players:
        print(player)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = get_players_from_response(response)

    sort_by = SortBy.POINTS
    sorted_finnish_players = sorted_finnish_players(players, sort_by)

    print_players(players)

if __name__ == "__main__":
    main()
