# Created by Michal Niemiec michal.niemiec.it@gmail.com
# I created this little "game" while learning python
# This project is based on project from book "Python Crash Course" and I modified it quite a bit.

import sys
import pygame

from pygame.locals import *
from settings import *
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien_2 import Alien2
from alien_3 import Alien3
from game_stats import GameStats
from time import *
from button import Button
from scoreboard import Scoreboard

clock = pygame.time.Clock()


class SpaceImpact:
    """Main class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height),
                                              HWSURFACE | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption("Space Impact")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet_1()
        self._create_fleet_2()
        self._create_fleet_3()

        # Set the background image
        self.bg_image = self.settings.bg_image
        self.imageship = self.ship.image

        # Instance to store game statistic.
        self.stats = GameStats(self)
        # Draw the score information.
        self.scoreboard = Scoreboard(self)
        self.scoreboard.show_score()

        # Make the Play button.
        self.play_button = Button(self)

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_aliens()
                self._update_bullets()

            # Redraw the screen during each pass through the loop.
            self._update_screen()

    def _check_events(self):
        """Respond to keypress and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to keydown events."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.settings.initialize_dynamic_settings()
            self.stats.game_active = True
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_hearts()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)
        # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            self.ship.center_ship()
            self._create_fleet_1()
            self._create_fleet_2()
            self._create_fleet_3()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _create_fleet_1(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self, self.settings)
        self.aliens.add(alien)
        alien = Alien(self, self.settings)
        self.aliens.add(alien)
        alien = Alien(self, self.settings)
        self.aliens.add(alien)

    def _create_fleet_2(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien_2 = Alien2(self, self.settings)
        self.aliens.add(alien_2)

    def _create_fleet_3(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien_3 = Alien3(self, self.settings)
        self.aliens.add(alien_3)

    def _ship_hit(self):
        """Respong to the ship being hit by an alien."""

        if self.stats.ships_left > 0:
            # Lower ships left.
            self.stats.ships_left -= 1
            self.scoreboard.prep_hearts()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self.ship.center_ship()
            self._create_fleet_1()
            self._create_fleet_2()
            self._create_fleet_3()

            print(self.stats.ships_left)
            # Pause.
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_aliens(self):
        """Update the position of all liens in the fleet."""
        self.aliens.update()
        # Look for alien-ship collision.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _update_bullets(self):
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        # Delete bullets that are off the screen
        for bullet in self.bullets.copy():
            if bullet.rect.right >= resolution_width * 1.1:
                self.bullets.remove(bullet)

        if not self.aliens:
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()

            self._create_fleet_1()
            self._create_fleet_2()
            self._create_fleet_3()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""

        self.screen.blit(pygame.transform.scale
                         (self.bg_image, [self.settings.screen_width, self.settings.screen_height]), (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        self.scoreboard.show_score()
        # Delete aliens that are off the screen
        for alien in self.aliens.copy():
            if alien.rect.right < 0:
                self.aliens.remove(alien)

        # Lines of code to show FPS counter
        # font = pygame.font.Font(None, 30)
        # fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
        # self.screen.blit(fps, (50, 50))

        # Regulate speed of the game by limiting FPS count.
        clock.tick(60)

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make the most recently draw screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    si = SpaceImpact()
    si.run_game()
