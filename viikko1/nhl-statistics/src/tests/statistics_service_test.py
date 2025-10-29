import unittest
from statistics_service import StatisticsService, SortBy
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

    def test_top_returns_correct_player_by_points(self):
        top_players = self.statistics_service.top(1, SortBy.POINTS)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_returns_correct_players_by_points(self):
        top_players = self.statistics_service.top(3, SortBy.POINTS)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_returns_correct_player_by_goals(self):
        top_players = self.statistics_service.top(1, SortBy.GOALS)
        self.assertEqual(top_players[0].name, "Lemieux")

    def test_top_returns_correct_player_by_assists(self):
        top_players = self.statistics_service.top(1, SortBy.ASSISTS)
        self.assertEqual(top_players[0].name, "Gretzky")

    def test_top_returns_error_if_invalid_enum(self):
        with self.assertRaises(ValueError):
            self.statistics_service.top(1, "points")
        
