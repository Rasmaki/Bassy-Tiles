import pygame
from LevelGenerator import LevelGenerator
from Tile import Tile


clock = pygame.time.Clock()
red = 255, 0, 0
white = 255, 255, 255
pygame.mixer.init()
spawn_sound = pygame.mixer.Sound('Audio/Blop.mp3')
pygame.font.init()
sysfont = pygame.font.get_default_font()


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
        self.columns = columns
        self.borderCol = 169, 169, 169
        self.max_row_tiles = 1
        self.tile_width = self.x2 / self.columns
        self.tile_height = 400
        self.tile_col = 255, 255, 255
        self.last_tile_y = 0
        self.bpm = 132
        self.fps = 120
        self.move_factor = 1 * (self.tile_height / 60) / self.fps * self.bpm  # self.tile_height / ( self.bpm / 60 )
        self.last_tile_columns = []
        self.counter = 0
        self.font = pygame.font.SysFont('Merriweather', 24)
        self.img = self.font.render('SCORE:', True, red)
        self.index = 0
        self.bass_line = []

    def display_board(self):
        distance = self.x2 / self.columns
        for i in range(self.columns - 1):
            from_pos = distance * (i + 1), 0
            to_pos = distance * (i + 1), self.height
            pygame.draw.line(self.display, self.borderCol, from_pos, to_pos, 5)

    def spawn_tile(self):
        if len(self.tiles) == 0 or self.last_tile_y + self.move_factor > 0:
            row = LevelGenerator.next_cycle(self.columns, self.max_row_tiles, False, self.last_tile_columns)
            self.last_tile_columns = []
            for i in range(self.columns):
                if row[i] == 1:
                    self.last_tile_columns.append(i)
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
        self.img = self.font.render('SCORE: ' + str(self.counter), True, red)
        self.display.blit(self.img, (1600, 100))
        self.counter += 1

    def handle_mouse_interaction(self, is_pressed):
        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.tiles:
            t.check_click(mouse_x, mouse_y, is_pressed)
        if is_pressed:
            self.index += 1
            print(self.index)
            self.bass_line[self.index].play()
            if self.index >= 63:
                self.index = 0

    def audio(self):
        for n in range(1, 65):
            self.bass_line.append(pygame.mixer.Sound('Audio/' + str(n) + '.wav'))




