import pygame

chosen_resolution = input(
    """Choose resolution in pixels (game will run in a window, so resolutions are lower):
A - Width: 1152px Height: 648px
B - Width: 1792px Height: 1008px
C - Width: 3712px Height: 2088px
"""
)

if chosen_resolution.upper() == 'A':
    resolution_width = 1152
    resolution_height = 648
elif chosen_resolution.upper() == "B":
    resolution_width = 1792
    resolution_height = 1008
elif chosen_resolution.upper() == "C":
    resolution_width = 3712
    resolution_height = 2088
else:
    print("Resolution not selected. Please restart")

# resolution_width = 1152
# resolution_height = 648


class Settings:
    """A class to store all settings for Space Impact."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        # This line is needed to avoid error: No video mode has been set
        self.screen = pygame.display.set_mode((0, 0))
        self.screen_width = resolution_width
        self.screen_height = resolution_height
        self.bg_image = pygame.image.load("images/background_1.png").convert()

        # Bullet settings
        self.bullet_speed = self.screen_width * 0.01
        self.bullet_width = self.screen_width * 0.02
        self.bullet_height = self.screen_height * 0.02
        self.bullet_color = (0, 0, 0)

        # Speed of an alien
        self.alien_speed = self.screen_width * 0.003
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # Ship Settings
        self.ships_limit = 3
        self.score_scale = 1.1
        self.initialize_dynamic_settings()

    def increase_speed(self):
        """Increase speed settings."""
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)

    def initialize_dynamic_settings(self):
        """Initialize settings that change throught the game."""
        self.alien_speed = self.screen_width * 0.003
        self.alien_points = 10
