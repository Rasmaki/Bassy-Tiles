import pygame
from pygame.locals import *
import sys
from Gameboard import GameBoard
from Sound import Sound
pygame.init()

columns = 5
background_col = 0, 0, 0
board = GameBoard(columns)
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')
pumpit = Sound('Audio/Give_a_Little_Love.mp3')
clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            #spawn_sound.play()
            print('click')
        board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)
    pumpit.play()
    board.spawn_tile()
    board.display.fill(background_col)
    board.update()
    board.display_board()
    board.surface.blit(board.display, (0, 0))
    pygame.display.update()
