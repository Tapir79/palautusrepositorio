# PlayerReader-luokan vastuulla on hakea JSON-muotoiset
# pelaajat konstruktorin parametrin
# kautta annetusta osoitteesta ja muodostaa niistä Player-olioita.
# Tämä voi tapahtua esimerkiksi luokan get_players-metodissa.

import requests

from player import Player


class PlayerReader:
    """Class to read player data from a given URL."""

    def __init__(self, url: str):
        self.url = url

    def get_raw_data(self):
        """Return raw JSON data from the API."""
        return requests.get(self.url, timeout=10).json()

    def get_players(self):
        """Fetch player data from the URL and return a list of Player objects."""
        response = self.get_raw_data()
        players = [Player(player_dict) for player_dict in response]
        return players
