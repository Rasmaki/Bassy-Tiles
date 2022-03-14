import pygame
from pygame.locals import *
import sys
from Menu import Menu
pygame.init()
clock = pygame.time.Clock()
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')
pygame.font.init()
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont('Helvetica', 24)
white = 255, 255, 255
score = 0

game_over = True
running = True
start = Menu()


def show_game_over():
    waiting = True
    while waiting:
        clock.tick(120)
        for event1 in pygame.event.get():
            start.handle_mouse_interaction(event1.type == pygame.MOUSEBUTTONDOWN)
            if event1.type == pygame.QUIT or event1.type == KEYDOWN and event1.key == K_ESCAPE:
                sys.exit()
            if event1.type == pygame.MOUSEBUTTONDOWN and start.start_button.is_pressed:
                spawn_sound.play()
                waiting = False
        start.screen.blit(start.bg_img, (0, 0))
        display_score()
        start.initialise()
        start.draw()
        pygame.display.update()


def display_score():
    score_text = font.render('LAST SCORE: ' + str(score), True, white)
    start.screen.blit(score_text, (start.width*5/7, start.height*5/7))


while running:
    if game_over:
        start = Menu()
        show_game_over()
        columns = 5
        start.board.audio()
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        start.board.handle_mouse_interaction(event.type == pygame.MOUSEBUTTONDOWN)
    start.board.display.blit(start.board.bg_img, (0, 0))
    start.board.spawn_tile()
    start.board.update()
    start.board.display_board()
    pygame.display.update()
    game_over = False
    for t in start.board.tiles:
        if t.y > 1000 and not t.is_pressed:
            score = start.board.counter
            game_over = True
