import pygame
from pygame.locals import *
import sys
import os

pygame.init()
size = game_width, game_height = 1920, 1080
screen = pygame.display.set_mode(size)


# Colors
white = 255, 255, 255
blue = 0, 0, 255
turquoise = 125, 125, 255
black = 0, 0, 0
soft_orange = 125, 0, 25
red = 255, 0, 0
dark_red = 80, 0, 0
objGroup = []


class Block(pygame.sprite.Sprite):
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

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.image.fill(black)

    def move_down(self):
        if self.block_y < 800:
            self.block_y += 10
            self.image.fill(red)

    def draw(self, surface):
        surface.blit(self.image, (self.block_x, self.block_y))


clock = pygame.time.Clock()
tile_group = pygame.sprite.Group()
tile = Block(blue, 50, 50, 1000, 540)
tile_group.add(tile)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYUP and event.type == K_ESCAPE:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for s in tile_group:
                tile.check_click(event.pos)

    tile.move_down()
    tile_group.update()
    tile.draw(screen)
    pygame.display.update()
    clock.tick(40)
