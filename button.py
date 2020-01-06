import pygame.font
from settings import Settings


class Button:

    def __init__(self, si_game):
        """Initialize button attributes."""
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        # Set the dimensions and properties of the button.
        self.width = 5 * self.settings.screen_width*0.1
        self.height = 1 * self.settings.screen_height*0.1
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg()

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on thr button."""
        self.msg_image = pygame.image.load("images/start.png")
        self.msg_image = pygame.transform.scale(self.msg_image, (214*int(self.settings.screen_width*0.0035),
                                                60*int(self.settings.screen_width*0.0035)))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.blit(self.msg_image, self.msg_image_rect)
