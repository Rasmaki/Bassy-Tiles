import pygame

pygame.font.init()
default_font = pygame.font.get_default_font()


class Key:
    def __init__(self, char, value, font):
        self.char = char
        self.value = value
        self.is_pressed = False
        self.is_wrong = False
        self.font = font
        self.col = 255, 20, 147
        self.col_if_pressed = 64, 224, 208
        self.col_if_wrong = 255, 0, 0

    def blit(self, screen, position):
        render = self.font.render(self.char, True, self.col)
        if self.is_wrong:
            render = self.font.render(self.char, True, self.col_if_wrong)
        elif self.is_pressed:
            render = self.font.render(self.char, True, self.col_if_pressed)
        screen.blit(render, position)

    def handle_press(self, event):
        if event.type == pygame.KEYDOWN and event.key == self.value:
            self.is_pressed = True
            print("pressed: " + self.char)
            print(self.is_pressed)
        elif event.type == pygame.KEYDOWN and not event.key == self.value:
            self.is_pressed = False

