import pygame
from pygame.locals import *
import sys
import random

# Colors
white = 255, 255, 255
blue = 0, 0, 255
turquoise = 125, 125, 255
black = 0, 0, 0
soft_orange = 125, 0, 25
red = 255, 0, 0
dark_red = 80, 0, 0

y1 = 300
y2 = 1920
bpm = 120
mpb = 1/bpm
mspb = mpb*60000

pygame.init()
size = game_width, game_height = 1920, 1080
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, block_x, block_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.block_x = block_x
        self.block_y = block_y
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.center = [block_x, block_y]
        self.speed = 4

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.image.fill(black)
            tile_group.add(Block(red, 50, 50, random.randrange(y1, y2, (round((y2 - y1) / 4))), 50))
            self.kill()

    def update(self):
        self.rect.y += self.speed


tile_group = pygame.sprite.Group()
tile = Block(red, 50, 50, random.randrange(y1, y2, (round((y2 - y1) / 4))), 50)
tile_group.add(tile)
surface_size = 1920, 1080
surface = pygame.Surface(surface_size)
surface.fill(black)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for s in tile_group:
                s.check_click(event.pos)
    screen.blit(surface, (0, 0))
    tile_group.draw(screen)
    tile_group.update()
    pygame.display.update()
    clock.tick(144)
