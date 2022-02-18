import pygame
import pygame
from pygame.locals import *
import sys
import os


class Tile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, x, y):

        pygame.sprite.Sprite.__init__(self)
        self.default_col = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.default_col)
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.rect.center = [x, y]
        self.is_pressed = False
        self.is_hovered = False
        self.hover_col = 0, 191, 255
        self.pressed_col = 100, 150, 255

    def check_click(self, x, y, is_pressed):
        # print(self.block_y)
        if self.is_colliding(x, y):
            self.is_hovered = True
            if is_pressed:
                self.is_pressed = True
        else:
            self.is_hovered = False

    def move_down(self):
        self.y += 1

    def draw(self, surface):
        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image.fill(self.default_col)

        surface.blit(self.image, (self.x, self.y))

    def is_colliding(self, x, y):
        if self.y < y < self.y + self.height:
            if self.x < x < self.x + self.width:
                return True

        return False
