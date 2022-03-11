import pygame
from pygame.locals import *
import sys
from Gameboard import GameBoard
from Sound import Sound
from Menu import Menu
pygame.init()

columns = 5
background_col = 0, 0, 0
green = 0, 255, 0
board = GameBoard(columns)
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')
music = Sound('Audio/Give_a_Little_Love.mp3')
clock = pygame.time.Clock()
Start = Menu()

while 1:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            spawn_sound.play()
        Start.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)
    Start.screen.fill(background_col)
    Start.initialise()
    Start.surface.blit(Start.screen, (0, 0))
    pygame.display.update()

    while Start.initialise():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)
        clock.tick(120)
        music.play()
        board.spawn_tile()
        board.display.fill(background_col)
        board.update()
        board.display_board()
        board.surface.blit(board.display, (0, 0))
        pygame.display.update()
