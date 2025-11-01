from ast import List
from enum import Enum


class SortBy(Enum):
    """Enumeration for sorting criteria."""
    POINTS = 1
    GOALS = 2
    ASSISTS = 3
    NAME = 4


def get_sort_key(player, sort_by: SortBy = SortBy.POINTS):
    """Return the sorting key based on the specified criteria."""
    mapping = {
        SortBy.POINTS: player.points,
        SortBy.GOALS: player.goals,
        SortBy.ASSISTS: player.assists,
        SortBy.NAME: player.name
    }
    return mapping[sort_by]


class PlayerStats:
    """Class to handle player statistics."""

    def __init__(self, reader):
        self._players: List = reader.get_players()

    def _filter_by_nationality(self, nationality: str):
        return [player for player in self._players if player.nationality == nationality]

    def top_scorers_by_nationality(self, nationality: str):
        """"Return top scorers filtered by nationality"""
        national_players = self._filter_by_nationality(nationality)

        return sorted(
            national_players,
            reverse=True,
            key=lambda player: get_sort_key(player, SortBy.POINTS))

    def top_scorers_sorted(self, sort_by: SortBy,):
        """"Return top scorers by goals filtered by nationality"""
        return sorted(
            self._players,
            reverse=True,
            key=lambda player: get_sort_key(player, sort_by))
