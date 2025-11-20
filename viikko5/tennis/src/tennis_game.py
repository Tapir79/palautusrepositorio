from enum import Enum

class TiedScore(str, Enum):
    LOVE_ALL = "Love-All"
    FIFTEEN_ALL = "Fifteen-All"
    THIRTY_ALL = "Thirty-All"
    DEUCE = "Deuce"

class PointName(str, Enum):
    LOVE = "Love"
    FIFTEEN = "Fifteen"
    THIRTY = "Thirty"
    FORTY = "Forty"

class Player(str, Enum):
    PLAYER1 = "player1"
    PLAYER2 = "player2"

DEUCE = 3
ADVANTAGE = 4


class TennisGame:
    def __init__(self, player1_name:str, player2_name:str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    #--- Public Methods ---#

    def won_point(self, player_name:str) -> int:
        if player_name == Player.PLAYER1:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self) -> str:
        if self._points_are_equal():
            return self._tied_message()
        if self._player_has_advantage():
            return  self._advantage_or_win_message()
        
        return self._regular_score_message()

    #--- Private Methods ---#

    def _points_are_equal(self) -> bool:
        return self.player1_points == self.player2_points

    def _tied_message(self) -> str:
        if self.player1_points >= DEUCE:
            return TiedScore.DEUCE

        player1_points = {
            0: TiedScore.LOVE_ALL,
            1: TiedScore.FIFTEEN_ALL,
            2: TiedScore.THIRTY_ALL,
        }

        score = player1_points[self.player1_points]
        return score

    def _player_has_advantage(self):
        return (self.player1_points >= ADVANTAGE 
                or self.player2_points >= ADVANTAGE)
    
    def _advantage_or_win_message(self):
        score_difference = self.player1_points - self.player2_points
        leader = (Player.PLAYER1.value 
                if score_difference > 0 
                else Player.PLAYER2.value)
        
        if abs(score_difference) == 1:
            return f"Advantage {leader}"
            
        return f"Win for {leader}"

    def _regular_score_message(self):
        score_names = {
            0: PointName.LOVE,
            1: PointName.FIFTEEN,
            2: PointName.THIRTY,
            3: PointName.FORTY
        }

        player1_scorename = score_names[self.player1_points].value
        player2_scorename = score_names[self.player2_points].value

        return f"{player1_scorename}-{player2_scorename}" 
