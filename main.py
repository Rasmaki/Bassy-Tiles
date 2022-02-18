import pygame
from pygame.locals import *
import sys
from Gameboard import GameBoard
from Sound import Sound
pygame.init()

columns = 6
background_col = 0, 0, 0
board = GameBoard(columns)
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')
pumpit = Sound('Audio/pump_it.mp3')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            spawn_sound.play()
        board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)

    board.spawn_tile()
    board.display.fill(background_col)
    board.update()
    board.display_board()
    board.surface.blit(board.display, (0, 0))
    pygame.display.update()
