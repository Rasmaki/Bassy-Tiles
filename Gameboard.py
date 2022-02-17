import pygame

from Tile import Tile

red = 255, 0, 0


class Gameboard():
    def __init__(self, collums):
        self.collums = collums
        self.tiles = []
        self.tile = Tile(red, 100, 100, 500, 500)
        self.speed = 1
        self.acceleration = 1

    def start(self):
        print("start")

    def addTile(self, tile):
        self.tiles.append(tile)
