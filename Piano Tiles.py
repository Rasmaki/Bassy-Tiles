import pygame
from pygame.locals import *
import sys

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
        self.speed = 10

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            self.image.fill(black)

    def update(self):
        self.rect.y += self.speed
        pygame.sprite.Sprite.update(self)


clock = pygame.time.Clock()
tile_group = pygame.sprite.Group()
tile = Block(blue, 50, 50, 1000, 540)
tile_group.add(tile)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYUP and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for s in tile_group:
                tile.check_click(event.pos)

    tile_group.draw(screen)
    tile_group.update()
    pygame.display.update()
    pygame.display.flip()
    clock.tick(10)
