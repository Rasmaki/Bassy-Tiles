import pygame
from pygame.locals import *
import sys
import os

import LevelGenerator
from Gameboard import GameBoard
from Sound import Sound
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
columns = 6

clock = pygame.time.Clock()
tiles = []
board = GameBoard(columns)

counter = 0
delay = 30
bpm = 174*2
mspb = 60000 / bpm
passed_ms = 0
spawn_sound = pygame.mixer.Sound('Blop.mp3')
pumpit = Sound('pump_it.mp3')


def check_bpm():
    if pygame.time.get_ticks() % mspb <= 1:
        board.spawn_tile()
        #pumpit.play()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            spawn_sound.play()

        board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)

    board.spawn_tile()
    counter += 1
    board.display.fill(black)
    board.update()
    board.display_board()
    board.surface.blit(board.display, (0, 0))
    pygame.display.update()
