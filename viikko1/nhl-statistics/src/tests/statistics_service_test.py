import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.statistics_service = StatisticsService(PlayerReaderStub())

    def test_search_by_existing_name_returns_correct_player(self):
        player = self.statistics_service.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.team, "EDM")

    def test_search_by_non_existing_name_returns_none(self):
        player = self.statistics_service.search("Guybrush")
        self.assertIsNone(player)

    def test_team_count_is_correct(self):
        team = self.statistics_service.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_returns_correct_player(self):
        top_players = self.statistics_service.top(1)
        self.assertEqual(top_players[0].name, "Gretzky")
        
