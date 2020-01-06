class GameStats:
    """Track player's statistics."""

    def __init__(self, si_game):
        """Initialize statistics."""
        self.settings = si_game.settings
        self.reset_stats()
        # Starts game in an inactive state.
        self.game_active = False
        # High score is stored in high_score.txt
        self.high_score = open("high_score.txt", "r+")

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ships_limit
        self.level = 1
        self.score = 0
