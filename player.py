from typing_extensions import Self
import pygame,os

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('/Users/gerrardxcc/Desktop/AppDev/Space-Invaders/images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.react.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.react.x -= self.speed

    def update(self):
        self.get_input()