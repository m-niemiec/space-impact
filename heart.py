import pygame
from settings import Settings
from pygame.sprite import Sprite


class Heart(Sprite):
    """A class to manage hearts."""

    def __init__(self, si_game):
        """Initialize the heart and it's properties."""
        super().__init__()
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = Settings()

        # Load the ship image and get its react.
        self.image = pygame.image.load("images/heart.png")
        self.image = pygame.transform.scale(self.image, (30*int(self.settings.screen_width*0.002),
                                            30*int(self.settings.screen_width*0.002)))
        self.rect = self.image.get_rect()
