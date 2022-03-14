import pygame


class Tile(pygame.sprite.Sprite):
    """Rect-style spirtes which are moving down.

    Attributes:
        default_col (tuple[int, int, int]): saves the default color of the tile.
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
        self.image = pygame.Surface([width, height])
        self.image.fill(self.default_col)
        self.rect = self.image.get_rect()
        self.height = height
        self.width = width
        self.y = y
        self.x = x
        self.rect.center = [x, y]
        self.is_pressed = False
        self.is_hovered = False
        self.hover_col = 0, 191, 255
        self.pressed_col = 100, 150, 255

    def check_click(self, x, y, is_pressed):
        """Checks if the coordinates of the cursor are colliding with the tile.
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
        return False

    def move_down(self, amount):
        """Makes the tile move down."""

        self.y += amount

    def draw(self, surface):
        """Fill the button accordingly to the mouse interaction.
        If the tile is pressed it is filled with the 'pressed' color.
        If the tile is hovered it is filled with the 'hovered' color.
        If the tile is neither pressed or hovered, it will remain the image.

        Arguments:
            :param surface: surface of the game.
            :return -> None

        """

        if self.is_pressed:
            self.image.fill(self.pressed_col)
        elif self.is_hovered:
            self.image.fill(self.hover_col)
        else:
            self.image.fill(self.default_col)

        surface.blit(self.image, (self.x, self.y))

    def is_colliding(self, x, y):
        """Checks if the cursor is within the tile-object.

        Arguments:
            :param x: x-coordinates of the cursor.
            :param y: y-coordinates of the cursor.
            :return -> None

        """

        if self.y < y < self.y + self.height:
            if self.x < x < self.x + self.width:
                return True
        return False
