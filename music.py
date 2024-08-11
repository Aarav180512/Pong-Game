import pygame as pg


class Music:
    def __init__(self, music_file):
        pg.mixer.init()

        self.music_file = music_file
        self.volume = 0.1
        self.mute = 0.0

    def play_music(self):
        pg.mixer.music.load(self.music_file)
        pg.mixer.music.play(loops=-1)

    def play(self):
        pg.mixer.music.set_volume(self.volume)

    def mute(self):
        pg.mixer.music.set_volume(self.mute)
