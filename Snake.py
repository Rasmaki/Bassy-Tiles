import pygame
import sys

pygame.init()

lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0
fps = 144
size = width, height = 1080, 720
screen = pygame.display.set_mode(size)
white = 255, 255, 255
blue = 0, 255, 0
black = 0, 0, 0
red = 255, 0, 0

pygame.draw.rect(screen, blue, (lead_x, lead_y, 10, 10))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_y_change = 0
                lead_x_change = -20/fps
            if event.key == pygame.K_RIGHT:
                lead_y_change = 0
                lead_x_change = 20/fps
            if event.key == pygame.K_UP:
                lead_x_change = 0
                lead_y_change = -20/fps
            if event.key == pygame.K_DOWN:
                lead_x_change = 0
                lead_y_change = 20/fps
    lead_x += lead_x_change
    lead_y += lead_y_change

    screen.fill(white)
    if lead_x >= width:
        lead_x = 0
    elif lead_x < 0:
        lead_x = width
    elif lead_y >= height:
        lead_y = 0
    elif lead_y < 0:
        lead_y = height
    else:
        pygame.draw.rect(screen, black, [lead_x, lead_y, 10, 10])
    pygame.display.flip()



