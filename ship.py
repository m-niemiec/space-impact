import pygame
from settings import Settings


class Ship:
    """A class to manage the ship."""

    def __init__(self, si_game):
        """Initialize the ship and set its starting positon."""
        self.screen = si_game.screen
        self.screen_rect = si_game.screen.get_rect()
        self.settings = Settings()

        # Load the ship image and get its react.
        self.image = pygame.image.load("images/ship_1.png")
        self.image = pygame.transform.scale(self.image, (80*int(self.settings.screen_width*0.0019),
                                            56*int(self.settings.screen_width*0.0019)))
        self.rect = self.image.get_rect()

        # This value is needed later to make ship appear in exact center in every resolution
        # v = 56*int(self.settings.screen_width*0.0019)

        # Start each new ship at the left center of the screen.
        self.rect.center = (int(self.settings.screen_width*0.07), int(self.settings.screen_height*0.5))

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.ship_speed = self.settings.screen_width*0.005

    def update(self):
        """Update ship's position based on the movement flag."""
        if self.moving_right and self.rect.x < self.settings.screen_width*0.85:
            self.rect.x += self.ship_speed
        elif self.moving_left and self.rect.x > 0:
            self.rect.x -= self.ship_speed
        elif self.moving_up and self.rect.y > 0:
            self.rect.y -= self.ship_speed
        elif self.moving_down and self.rect.y < self.settings.screen_height*0.84:
            self.rect.y += self.ship_speed

    def blitme(self):
        """Draw ship at its current location."""

        # Little system that will make sure that ship will be scaled with resolution
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.center = (int(self.settings.screen_width*0.07), int(self.settings.screen_height*0.5))
        self.x = float(self.rect.x)
