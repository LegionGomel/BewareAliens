import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for control bullets from ship"""
    def __init__(self, ai_settings, screen, ship):
        """Creates bullet object at current ship position"""
        super(Bullet, self).__init__()
        self.screen = screen
        # Create bullet at (0,0) and assign right position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Bullet position stored as float
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move bullet up on screen"""
        # Renew bullet position in float format
        self.y -= self.speed_factor
        # Renew rectangle position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
