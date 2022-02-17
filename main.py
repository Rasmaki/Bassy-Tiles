import pygame
from pygame.locals import *
import sys
import os
from Gameboard import Gameboard
from Tile import Tile

pygame.init()
# size = game_width, game_height = 1920, 1080
# screen = pygame.display.set_mode(size)

# Colors
white = 255, 255, 255
blue = 0, 0, 255
turquoise = 125, 125, 255
black = 0, 0, 0
soft_orange = 125, 0, 25
red = 255, 0, 0
dark_red = 80, 0, 0

clock = pygame.time.Clock()
tiles = []
board = Gameboard(9)

counter = 0
delay = 50
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        #elif event.type == pygame.MOUSEBUTTONDOWN:
        #    board.spawn_tile()
        #     mousePos = pygame.mouse.get_pos()
        #     mouseX = mousePos[0]
        #     mouseY = mousePos[1]
        #     tiles.append(Tile(red, 50, 50, mouseX, mouseY))
    if counter == delay:
        counter = 0
        board.spawn_tile()

    counter += 1
    board.display.fill(black)
    board.update()
    board.display_board()
    board.surface.blit(board.display, (0, 0))
    pygame.display.update()
    clock.tick(100)
