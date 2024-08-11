from variables import *
import pygame as pg


class Paddle:
    def __init__(self, game, x, y, width, height):
        self.game = game
        self.screen = game.screen
        self.x = self.original_x =  x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self):
        pg.draw.rect(self.screen, PADDLE_COLOR,
                     (self.x, self.y, self.width, self.height)
                     )

    def move_up(self):
        self.y -= PADDLE_VEL

    def move_down(self):
        self.y += PADDLE_VEL

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y

