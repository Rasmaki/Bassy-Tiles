import pygame
import sys
from Gameboard import GameBoard

black = 0, 0, 0
white = 255, 255, 255
pygame.font.init()
sysfont = pygame.font.get_default_font()


class Menu:
    """Start Menu of the game. Displays background image, start- and exit-buttons, a welcome message, score
    and is used to initiate a new game-board.

    Attributes:
        screen (Union[]): Saves the mode of the display.
        width (Optional[int]): Saves the width of the display.
        height (Optional[int]): Saves the height of the display.
        bg_img (Union[Surface, SurfaceType]): Loads an Image and transforms it to width and height.
        start_button (Button): creates a start button.
        exit_button (Button): creates an exit button.
        column (int): defines the number of columns.
        board (GameBoard): creates a new board.
        score (int): Sets the game-score to 0 in the beginning.
        font (Font): initialises Helvetica font.
        welcome_msg (Union[Surface, SurfaceType]): Renders welcome message into a surface.

    """

    def __init__(self):
        """Holds parameters and attributes of the Menu class"""

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.width = pygame.display.get_surface().get_width()
        self.height = pygame.display.get_surface().get_height()
        self.bg_img = pygame.image.load('img/bg_menu.png')
        self.bg_img = pygame.transform.scale(self.bg_img, (self.width, self.height))
        self.start_button = Button(black, 200, 50, self.width*5/7, self.height/4)
        self.exit_button = Button(black, 200, 50, self.width*6/7, self.height/4)
        self.button_group = [self.start_button, self.exit_button]
        self.column = 5
        self.board = GameBoard(self.column)
        self.score = 0
        self.font = pygame.font.SysFont('Helvetica', 24)
        self.welcome_msg = self.font.render('WELCOME TO BASSY TILES!', True, white)

    def initialise(self):
        """Draw the buttons on the Menu Screen. If the exit button is pressed, the game will exit.

        :param -> None
        :return -> None

        """

        for t in self.button_group:
            t.draw(self.screen)
        if self.exit_button.is_pressed:
            sys.exit()

    def draw(self):
        """Blit the button-text and the welcome message.
        Use parameters to create a dynamic picture for every resolution.

        :param -> None
        :return -> None

        """

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
        """Gets x,y position of the cursor, checks for mouse-clicks and collision with buttons.

        :param is_pressed: -> bool
        :return -> None

        """

        mouse_pos = pygame.mouse.get_pos()
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]
        for t in self.button_group:
            t.check_click(mouse_x, mouse_y, is_pressed)


class Button(pygame.sprite.Sprite):
    """Buttons displayed on the start screen.

        Attributes:
            default_col (tuple[int, int, int]): saves the default color of the button
            image (Union[Surface, SurfaceType, None]): Loads and saves an image for the buttons.
            rect (Union[Rect, RectType, None]): Creates an rect-style Object (Sprite).
            width (tuple[int, int]): Saves width of the sprite.
            height (tuple[int, int]): Saves height of the sprite.
            x (int): Saves x-position of the sprite.
            y (int): Saves x-position of the sprite.
            rect.center (tuple[int, int]): assigns x and y to the sprite.
            is_pressed (bool): the button is not yet pressed.
            is_hovered (bool): the button is not yet hovered over.
            hover_col (tuple[int, int, int]): color of the button getting hovered by the cursor.
            pressed_col (tuple[int, int, int]): color of the button getting pressed.
            font (Font): initialises Helvetica font.
            img1 (Union[Surface, SurfaceType]): Renders 'START' into a surface.
            img2 (Union[Surface, SurfaceType]): Renders 'EXIT' into a surface.

        """

    def __init__(self, color, width, height, x, y):
        """Holds parameters and attributes of the Button class.

        :param color: Sets the color of the button.
        :param width: Sets the width of the button.
        :param height: Sets the height of the button.
        :param x: Sets the x-position of the button.
        :param y: Sets the y-position of the button.

        """

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
        """Checks if the coordinates of the cursor are colliding with the button.
        Also checks if the mouse-button is pressed.

        Arguments:
            :param x: x-coordinates of the cursor.
            :param y: y-coordinates of the cursor.
            :param is_pressed: checks if the mouse-button is getting pressed.
            :return -> None

        """

        if self.is_colliding(x, y):
            self.is_hovered = True
            if is_pressed:
                self.is_pressed = True
        else:
            self.is_hovered = False

    def is_colliding(self, x, y):
        """Checks if the cursor is within the button-object.

        Arguments:
            :param x: x-coordinates of the cursor.
            :param y: y-coordinates of the cursor.
            :return -> None

        """

        if self.y < y < self.y + self.height:
            if self.x < x < self.x + self.width:
                return True

        return False

    def draw(self, surface):
        """Fill the button accordingly to the mouse interaction.
        If the button is pressed it is filled with the 'pressed' color.
        If the button is hovered it is filled with the 'hovered' color.
        If the button is neither pressed or hovered, it will remain the image.

        Arguments:
            :param surface: surface of the game.
            :return -> None

        """

        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image = pygame.image.load('img/menu_buttons.png')

        surface.blit(self.image, (self.x, self.y))
