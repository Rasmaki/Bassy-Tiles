import pygame
import pygame
from pygame.locals import *
import sys
import os

class Tile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, block_x, block_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.block_y = block_y
        self.block_x = block_x
        self.rect.center = [block_x, block_y]

    type = 1

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.image.fill(0, 0, 0)

    def move_down(self):
        self.block_y += 1

    def draw(self, surface):
        surface.blit(self.image, (self.block_x, self.block_y))
