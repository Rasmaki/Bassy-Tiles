import pygame
import sys


class Ellipse(pygame.sprite.Sprite):
    def __init__(self, e_lead_x, e_lead_y, e_x_change, e_y_change, e_width, e_height):
        self.e_lead_x = e_lead_x
        self.e_lead_y = e_lead_y
        self.e_x_change = e_x_change
        self.e_y_change = e_y_change
        self.e_width = e_width
        self.e_height = e_height
        self.ellipsis = ellipsis

    def e_dir(self):
        self.e_lead_x += self.e_x_change
        self.e_lead_y += self.e_y_change

    def move(self):
        self.ellipsis = pygame.draw.ellipse(screen, dark_red, [self.e_lead_x, self.e_lead_y, self.e_width, self.e_height])

    def check_collision(self):
        tile_list = ()
        tile_hit_list = pygame.sprite.spritecollide(rect, tile_list, True)
        for self.ellipsis in tile_hit_list:
            self.e_y_change = -self.e_y_change


# Init
pygame.init()
size = width, height = 1920, 1080
fps = 144
pixel = 100
Ball = Ellipse((width/2), 300, (40/fps), (40/fps), 20, 20)
screen = pygame.display.set_mode(size)

# Rectangle
rect_lead_x = width / 2
rect_lead_y = height * 3 / 4
lead_x_change = 0
rect_width = 100
rect_height = 20

# Colors
white = 255, 255, 255
blue = 0, 0, 255
turquoise = 125, 125, 255
black = 0, 0, 0
soft_orange = 125, 0, 25
red = 255, 0, 0
dark_red = 80, 0, 0

while 1:
    screen.fill(soft_orange)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -pixel/fps
            if event.key == pygame.K_RIGHT:
                lead_x_change = pixel/fps
        else:
            lead_x_change = 0

    # Collision Rectangle
    if rect_lead_x+rect_width >= width:
        rect_lead_x = width - rect_width
    elif rect_lead_x <= 0:
        rect_lead_x = 0

    # Init Rectangle
    rect_lead_x += lead_x_change
    rect = pygame.draw.rect(screen, black, [rect_lead_x, rect_lead_y, rect_width, rect_height])

    Ball.e_dir()
    Ball.move()
    pygame.display.flip()
