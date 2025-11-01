# PlayerReader-luokan vastuulla on hakea JSON-muotoiset pelaajat konstruktorin parametrin kautta annetusta osoitteesta ja muodostaa niistä Player-olioita.
# Tämä voi tapahtua esimerkiksi luokan get_players-metodissa.

import requests

from player import Player


class PlayerReader:
    def __init__(self, url: str):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        players = [Player(player_dict) for player_dict in response]
        return players
