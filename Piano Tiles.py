import pygame
import sys

pygame.init()
size = game_width, game_height = 1920, 1080
screen = pygame.display.set_mode(size)
#background = pygame.image.load("BG.png")
#pygame.mouse.set_visible(False)

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
        self.rect = self.image.get_rect()
        self.rect.center = [block_x, block_y]


tile_group = pygame.sprite.Group()

for i in range(50):
    tile = Block(blue, 50, 50*i, 100*i, 540)
    tile_group.add(tile)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
    # screen.blit(background, [0, 0])
    tile_group.draw(screen)

