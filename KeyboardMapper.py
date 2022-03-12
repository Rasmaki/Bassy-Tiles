import pygame.key

from Key import Key

pygame.font.init()
default_font = pygame.font.get_default_font()
font = pygame.font.SysFont(default_font, 60)

second = ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p', 'ü']
first = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ö', 'ä']
third = ['<', 'y', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '-']


class KeyboardMapper:
    def __init__(self, amount):
        self.amount = amount
        self.key_dict = {}
        self.init_keys()
        self.font = pygame.font.SysFont(default_font, 24)

    def init_keys(self):
        #Todo: Fix higher than 11 -> implement max collumns in menu
        for i in range(0, self.amount):
            key = ""
            if i < len(first):
                key = first[i]
                print("first")
            elif i < len(first) + len(second):
                key = second[i + len(first)]
                print("second")
            elif i < len(first) + len(second) + len(third):
                key = third[i + len(first) + len(second)]

            code = pygame.key.key_code(key)
            self.key_dict.update({key: Key(key, code, font)})

    def display_keys(self, screen, start, interval, height):
        start = start - (font.get_linesize()/2)
        count = 0
        for key in self.key_dict:
            self.key_dict[key].blit(screen, (start + interval * count, height))
            count += 1

    def handle_press(self, event):
        for key in self.key_dict:
            self.key_dict[key].handle_press(event)
