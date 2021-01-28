import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # Initialize a pygame, settings and create screen, ship objects
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Create button object
    play_button = Button(ai_settings, screen, "Play")
    # Create game_statistics and score board objects
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Create ship object
    ship = Ship(ai_settings, screen)
    # Create groups for bullets and aliens storing
    bullets = Group()
    aliens = Group()
    # Create alien fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Start main game cycle
    while True:
        # Tracking keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
