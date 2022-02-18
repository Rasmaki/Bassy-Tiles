import random

import pygame

from LevelGenerator import LevelGenerator
from Tile import Tile

red = 255, 0, 0


class Gameboard():
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
        self.tile = Tile(red, 100, 100, 500, 500)
        # self.tiles.append(self.tile)
        self.do_infinite = True
        self.speed = 1
        self.acceleration = 1
        self.columns = columns
        self.borderCol = 169, 169, 169
        self.max_row_tiles = self.columns / 2

    def display_board(self):
        distance = self.x2 / self.columns
        for i in range(self.columns - 1):
            from_pos = distance * (i + 1), 0
            to_pos = distance * (i + 1), self.height
            pygame.draw.line(self.display, self.borderCol, from_pos, to_pos, 5)

    def spawn_tile(self):
        rnd = random.randint(0, self.columns - 1)
        tile_width = self.x2 / self.columns
        tile_height = 250
        self.tiles.append(Tile((255, 255, 255), tile_width, tile_height, tile_width * rnd, - tile_height))
        last_added_index = len(self.tiles) - 1
        last_added_tile = self.tiles[last_added_index]
        #ToDo: Spawn next row when next tile move its y is greater than 0
        if last_added_tile.y + last_added_tile.width > 0:
            LevelGenerator.next_cycle(self.columns, self.max_row_tiles)


    # ToDo: delete tile if out of gameboard range
    def update(self):
        for t in self.tiles:
            t.move_down()
            if t.y > self.height:
                self.tiles.remove(t)
            t.draw(self.display)

    def handle_mouse_interaction(self, is_pressed):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.tiles:
            t.check_click(mouse_x, mouse_y, is_pressed)
