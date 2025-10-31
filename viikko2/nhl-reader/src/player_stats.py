from ast import List
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    NAME = 4

def get_sort_key(player, sort_by: SortBy = SortBy.POINTS):
    mapping = {
        SortBy.POINTS: player.points,
        SortBy.GOALS: player.goals,
        SortBy.ASSISTS: player.assists,
        SortBy.NAME: player.name
    }
    return mapping[sort_by]

class PlayerStats:
    def __init__(self, reader):
        self._players: List = reader.get_players()

    def _filter_by_nationality(self, nationality: str):
        return [player for player in self._players if player.nationality == nationality]
    
    def top_scorers_by_nationality(self, nationality: str):
        national_players = self._filter_by_nationality(nationality)

        return sorted(
         national_players, 
         reverse=True,
         key=lambda player: get_sort_key(player, SortBy.POINTS))