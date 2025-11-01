class Player:
    """Class representing an NHL player."""

    def __init__(self, player_dict):
        self.set_attributes(player_dict)

    def set_attributes(self, player_dict):
        """Set player attributes from a dictionary."""
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']

    @property
    def points(self):
        """Calculate total points for the player."""
        return self.goals + self.assists

    def __str__(self):
        """String representation of the player."""
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.points:3}"
