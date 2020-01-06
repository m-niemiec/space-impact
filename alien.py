import pygame
from pygame.sprite import Sprite
from settings import Settings
import random


class Alien(Sprite):
    """A class to represent a single alien."""

    def __init__(self, space_impact, settings):
        """Initialize alien and set it's starting position."""
        super().__init__()
        self.screen = space_impact.screen
        self.settings = settings

        # Load the alien image and set it's rect attribute.
        self.index = 0
        self.timer = 0
        self.image = []
        self.image.append(pygame.image.load('images/alien_1_1.png'))
        self.image.append(pygame.image.load('images/alien_2_2.png'))
        self.image = self.image[self.index]
        self.image = pygame.transform.scale(self.image, (80 * int(self.settings.screen_width * 0.0019),
                                            40 * int(self.settings.screen_width*0.0019)))
        self.rect = self.image.get_rect()

        random_height = random.uniform(0.09, 0.85)
        random_width = random.uniform(1.1, 2)
        self.rect.x = int(self.settings.screen_width * random_width)
        self.rect.y = int(self.settings.screen_height * random_height)

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to left side."""
        self.x -= self.settings.alien_speed
        self.rect.x = self.x

        if 0 <= self.timer <= 25:
            self.timer += 1
            self.index = 0

        elif 26 <= self.timer < 50:
            self.timer += 1
            self.index = 1
        else:
            self.timer = 0

        if self.index == 0:
            self.image = pygame.image.load("images/alien_1_1.png")
        if self.index == 1:
            self.image = pygame.image.load("images/alien_1_2.png")

        self.image = pygame.transform.scale(self.image, (80 * int(self.settings.screen_width * 0.0019),
                                            40 * int(self.settings.screen_width * 0.0019)))
