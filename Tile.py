import pygame
import pygame
from pygame.locals import *
import sys
import os


class Tile(pygame.sprite.Sprite):

    def __init__(self, color, width, height, block_x, block_y):

        pygame.sprite.Sprite.__init__(self)
        self.default_col = color
        self.image = pygame.Surface([width, height])
        self.image.fill(self.default_col)
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.block_y = block_y
        self.block_x = block_x
        self.rect.center = [block_x, block_y]
        self.is_pressed = False
        self.is_hovered = False
        self.hover_col = 100, 150, 255
        self.pressed_col = 0, 191, 255

    type = 1

    def check_click(self, x, y, event):
        #print(self.block_y)
        if self.rect.collidepoint(x, y):
            #print("check click")
            self.is_hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.is_pressed = True
            self.image.fill(self.pressed_col)

    def move_down(self):
        self.block_y += 1

    def draw(self, surface):
        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image.fill(self.default_col)

        surface.blit(self.image, (self.block_x, self.block_y))

    def is_colliding(self, x, y):
        print("test")