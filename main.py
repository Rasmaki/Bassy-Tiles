import pygame
from pygame.locals import *
import sys
from Gameboard import GameBoard
from Menu import Menu
pygame.init()
clock = pygame.time.Clock()
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')

game_over = True
running = True
background_col = 0, 0, 0


def show_game_over():
    start = Menu()
    start.screen.fill(background_col)
    waiting = True
    while waiting:
        clock.tick(120)
        for event1 in pygame.event.get():
            start.handle_mouse_interaction(event1.type == pygame.MOUSEBUTTONDOWN)
            if event1.type == pygame.QUIT or event1.type == KEYDOWN and event1.key == K_ESCAPE:
                sys.exit()
            if event1.type == pygame.MOUSEBUTTONDOWN:
                spawn_sound.play()
                waiting = False
        start.initialise()
        start.draw()
        start.surface.blit(start.screen, (0, 0))
        pygame.display.update()


while running:
    if game_over:
        show_game_over()
        columns = 5
        board = GameBoard(columns)
        board.audio()
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)
    board.spawn_tile()
    board.display.fill(background_col)
    board.update()
    board.display_board()
    board.surface.blit(board.display, (0, 0))
    pygame.display.update()
    game_over = False
    for t in board.tiles:
        if t.y > 1000 and not t.is_pressed:
            game_over = True
