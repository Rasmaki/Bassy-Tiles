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
    """Gameboard is a class to handle the game functions and parameters.
    Its Arguments makes the game highly customisable.

        Attributes:
            display (Union[Surface, SurfaceType]): Initialized pygame display
            width (Optional[int]): Gets the width of the display
            width (Optional[int]): Gets the height of the display
            bg_img (Union[Surface, SurfaceType]): Loads an Image and transforms it to width and height.
            x1 (int): upper left x-coordinate of the game-board
            y1 (int): upper left y- coordinate of the game-board
            x2 (int): down right x-coordinate of the game-board
            y2 (int): down right y-coordinate of the game-board
            tiles (int[]): Tiles which are rendered on the game-board
            columns (int): Number of columns on the game-board.
            borderCol (tuple[int, int, int]): The color of the game-boards borders/column-separations.
            max_row_tiles (int): Amount of tiles that should spawn in a row.
            tile_width (float): The width of all tiles.
            tile_height (int): The height of all tiles.
            tile_col (tuple[int, int, int]): The color of all tiles.
            last_tile_y (int): The height of the last spawned row, to know when to spawn a new one.
            bpm (int): The beats per minute in which the tile should spawn at.
            fps (int): The fps of the game to calculate the tile movement factor.
            move_factor (float): The speed of the tiles.
            last_tile_columns (list): Tiles to exclude at next row spawn.
            counter (int): In-game score system.
            font (Font): initialises Helvetica font.
            img (Union[Surface, SurfaceType]):
            index (int): Used to iterate through the bass-line list.
            bass_line (list): Stores all bass audio.


    """

    def __init__(self, columns):
        """Holds parameters and attributes of the GameBoard class.

        :param columns: create the game-board with a specific amount of columns

        """

        self.display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.bg_img = pygame.image.load('img/bg_ingame.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))
        self.x1 = 0
        self.y1 = 0
        self.x2 = self.width
        self.y2 = self.height
        self.tiles = []
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
        self.font = pygame.font.SysFont('Helvetica', 24)
        self.img = self.font.render('SCORE:', True, red)
        self.index = 0
        self.bass_line = []

    def display_board(self):
        """Method draws the the game-boards borders/column-separations.

        :param -> None
        :return -> None

        """

        distance = self.x2 / self.columns
        for i in range(self.columns - 1):
            from_pos = distance * (i + 1), 0
            to_pos = distance * (i + 1), self.height
            pygame.draw.line(self.display, self.borderCol, from_pos, to_pos, 5)

    def spawn_tile(self):
        """Method spawns new tiles when the last row spawned is fully visible.

        :param -> None
        :return -> None

        """

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
        """Method moves and draws the tiles. Also counts up the score. The tile gets an acceleration factor.

        :param -> None
        :return -> None

        """

        for t in self.tiles:
            t.move_down(self.move_factor)
            if t.y > self.height + self.tile_height:
                self.tiles.remove(t)
            t.draw(self.display)

        self.last_tile_y = self.tiles[len(self.tiles) - 1].y
        self.img = self.font.render('SCORE: ' + str(self.counter), True, red)
        self.display.blit(self.img, (1600, 100))
        self.counter += 1
        self.move_factor += 0.001

    def handle_mouse_interaction(self, is_pressed):
        """Method checks if tiles are hovered or pressed

        Arguments:
            :param is_pressed:  if the mouse is currently pressed
            :return -> None

        """

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.tiles:
            t.check_click(mouse_x, mouse_y, is_pressed)
        if is_pressed:
            self.index += 1
            self.bass_line[self.index].play()
            if self.index >= 63:
                self.index = 0

    def audio(self):
        """Initialises Audio. Creates a list of bass-sounds.

        :param -> None
        :return -> None

        """

        for n in range(1, 65):
            self.bass_line.append(pygame.mixer.Sound('Audio/' + str(n) + '.wav'))
