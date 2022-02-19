import pygame
from LevelGenerator import LevelGenerator
from Sound import Sound
from Tile import Tile

red = 255, 0, 0
spawn_sound = pygame.mixer.init()
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')


class GameBoard:
    def __init__(self, columns):
        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.surface = pygame.Surface((self.width, self.height))
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.width
        self.y2 = self.height
        self.tiles = []
        self.do_infinite = True
        self.speed = 1
        self.acceleration = 1
        self.columns = columns
        self.borderCol = 169, 169, 169
        self.max_row_tiles = 1
        self.tile_width = self.x2 / self.columns
        self.tile_height = 400
        self.tile_col = 255, 255, 255
        self.last_tile_y = 0
        self.bpm = 128
        # ToDo: not hardcoded fps (60)
        self.move_factor = self.bpm * 60 / self.tile_height
        self.last_tile_columns = []

    def display_board(self):
        distance = self.x2 / self.columns
        for i in range(self.columns - 1):
            from_pos = distance * (i + 1), 0
            to_pos = distance * (i + 1), self.height
            pygame.draw.line(self.display, self.borderCol, from_pos, to_pos, 5)

    def spawn_tile(self):
        if len(self.tiles) == 0 or self.last_tile_y + self.move_factor > 0:
            spawn_sound.play()
            row = LevelGenerator.next_cycle(self.columns, self.max_row_tiles, False, self.last_tile_columns)
            self.last_tile_columns = []
            for i in range(self.columns):
                if row[i] == 1:
                    self.last_tile_columns.append(i)
                    # ToDo: use move factor for accurate tile spawn
                    self.tiles.append(
                        Tile(self.tile_col,
                             self.tile_width,
                             self.tile_height,
                             self.tile_width * i,
                             self.last_tile_y - self.move_factor - self.tile_height))
                    self.last_tile_y = - self.tile_height

    def update(self):
        for t in self.tiles:
            t.move_down(self.move_factor)
            if t.y > self.height + self.tile_height:
                self.tiles.remove(t)
            t.draw(self.display)

        self.last_tile_y = self.tiles[len(self.tiles) - 1].y

    def handle_mouse_interaction(self, is_pressed):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.tiles:
            t.check_click(mouse_x, mouse_y, is_pressed)
