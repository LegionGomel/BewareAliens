import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class that represent one alien"""
    def __init__(self, ai_settings, screen):
        """Init alien and define starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load alien image and add rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Every alien appear at left upper screen corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Save alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Show alien at current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move alien to the right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
