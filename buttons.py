from variables import *
import pygame as pg


class Buttons:
    def __init__(self, game, font, text, position):
        self.screen = game.screen
        self.font = font
        self.text = text
        self.position = position
        self.rect = pg.Rect(position[0], position[1], BUTTON_WIDTH, BUTTON_HEIGHT)

    def draw(self):
        pg.draw.rect(self.screen, BUTTON_COLOR, self.rect)

        text_surface = self.font.render(self.text, True, BUTTON_TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)