import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize ship and starting position"""
        super(Ship, self).__init__()
        # Moving flag
        self.ai_settings = ai_settings
        self.moving_right = False
        self.moving_left = False
        self.screen = screen
        # Loading ship image and aquirind rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Every new ship starts from lower part of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # Moving flag

    def blitme(self):
        """Draw ship at current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Renew ship position using flag"""
        # Update float center, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        """Places ship at the center of bottom lower side"""
        self.center = self.screen_rect.centerx
