import pygame.font
from heart import Heart
from pygame.sprite import Group


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, si_game):
        """Initialize scorekeeping attributes."""
        self.si_game = si_game
        self.screen = si_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = si_game.settings
        self.stats = si_game.stats

        # Font settings for scoring information.
        self.text_color = (0, 0, 0)
        # Font "Pixeled" created by OmegaPC777.
        self.font = pygame.font.Font("pixeled.ttf", int(self.settings.screen_height*0.04))
        # Prepate the initial score image.
        self.prep_level()
        self.prep_score()
        self.prep_high_score()
        self.prep_hearts()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score)
        score_str = "{:,}".format(rounded_score)
        # Display the score at the top right of the screen.
        self.score_image = self.font.render(score_str, True, self.text_color)

    def prep_high_score(self):
        """Turn the high_score into a rendered image."""
        # rounded_high_score = round(self.stats.high_score)
        self.high_score = open("high_score.txt", "r")
        self.high_score = self.high_score.read()
        self.high_score_value = f"HIGH SCORE {self.high_score}"

        # Display the score at the top right of the screen.
        self.high_score_image = self.font.render(self.high_score_value, True, self.text_color)

    def prep_new_high_score(self):
        """Turn the high_score into a rendered image."""
        self.new_high_score = f"NEW HIGH SCORE {self.high_score} !"
        # Display the score at the top right of the screen.
        self.high_score_image = self.font.render(self.new_high_score, True, self.text_color)

    def prep_level(self):
        """Turn the level into a rendered image"""
        level_str = f" LEVEL {str(self.stats.level)}"
        self.level_image = self.font.render(level_str, True, self.text_color)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, (self.settings.screen_width*0.82, self.settings.screen_height*0.001))
        self.screen.blit(self.level_image, (self.settings.screen_width*0.812, self.settings.screen_height*0.06))
        self.screen.blit(self.high_score_image, (self.settings.screen_width*0.25, self.settings.screen_height*0.001))
        self.hearts.draw(self.screen)

    def check_high_score(self):
        """Check to see if there is a new high score."""
        if self.stats.score > int(self.high_score):
            self.high_score = self.stats.score
            self.high_score = str(self.high_score)

            self.high_score_file = open("high_score.txt", "r+")
            self.high_score_file.write(str(self.stats.score))

            self.prep_new_high_score()

    def prep_hearts(self):
        """Show how many hearts are left."""
        self.hearts = Group()
        for heart_number in range(self.stats.ships_left):
            heart = Heart(self.si_game)
            heart.rect.x = self.settings.screen_width*0.01 + heart_number * self.settings.screen_width*0.06
            heart.rect.y = self.settings.screen_width*0.01
            self.hearts.add(heart)
