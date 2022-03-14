import pygame
import sys
from Gameboard import GameBoard

black = 0, 0, 0
white = 255, 255, 255
pygame.font.init()
sysfont = pygame.font.get_default_font()


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.bg_img = pygame.image.load('img/bg_menu.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))
        self.game_loop = False
        self.start_button = Button(black, 200, 50, self.width*5/7, self.height/4)
        self.exit_button = Button(black, 200, 50, self.width*6/7, self.height/4)
        self.button_group = [self.start_button, self.exit_button]
        self.column = 5
        self.board = GameBoard(self.column)
        self.score = 0
        self.font = pygame.font.SysFont('Helvetica', 24)
        self.welcome_msg = self.font.render('WELCOME TO BASSY TILES!', True, white)

    def initialise(self):
        for t in self.button_group:
            t.draw(self.screen)
        if self.start_button.is_pressed:
            return True
        if self.exit_button.is_pressed:
            sys.exit()
        return False

    def draw(self):
        self.screen.blit(self.start_button.img1, (self.start_button.width / 2 + self.start_button.x -
                                                  pygame.font.Font.get_linesize(self.start_button.font),
                                                  self.start_button.height / 2 + self.start_button.y -
                                                  pygame.font.Font.get_height(self.start_button.font) / 2))
        self.screen.blit(self.exit_button.img2, (self.exit_button.width / 2 + self.exit_button.x -
                                                 pygame.font.Font.get_linesize(self.exit_button.font),
                                                 self.exit_button.height / 2 + self.exit_button.y -
                                                 pygame.font.Font.get_height(self.exit_button.font) / 2))
        self.screen.blit(self.welcome_msg, (self.width/7, self.height/7))

    def handle_mouse_interaction(self, is_pressed):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.button_group:
            t.check_click(mouse_x, mouse_y, is_pressed)


class Button(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.default_col = color
        self.image = pygame.image.load('img/menu_buttons.png')
        self.rect = self.image.get_rect()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect.center = [x, y]
        self.is_pressed = False
        self.is_hovered = False
        self.hover_col = 25, 5, 5
        self.pressed_col = 100, 150, 255
        self.font = pygame.font.SysFont('Helvetica', 24)
        self.img1 = self.font.render('START', True, white)
        self.img2 = self.font.render('EXIT', True, white)

    def check_click(self, x, y, is_pressed):
        if self.is_colliding(x, y):
            self.is_hovered = True
            if is_pressed:
                self.is_pressed = True
        else:
            self.is_hovered = False

    def is_colliding(self, x, y):
        if self.y < y < self.y + self.height:
            if self.x < x < self.x + self.width:
                return True

        return False

    def draw(self, surface):
        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image = pygame.image.load('img/menu_buttons.png')

        surface.blit(self.image, (self.x, self.y))
