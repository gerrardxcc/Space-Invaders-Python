import pygame,os

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('/Users/gerrardxcc/Desktop/AppDev/Space-Invaders/images/player.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)