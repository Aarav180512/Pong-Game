from variables import *
import pygame as pg


class Ball:
    def __init__(self, game, x, y, radius):
        self.game = game
        self.screen = game.screen
        self.x =  self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = MAX_BALL_VEL
        self.y_vel = 0

    def draw(self):
        pg.draw.circle(self.screen, BALL_COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
