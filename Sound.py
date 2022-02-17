import pygame


class Sound():
    def __init__(self, sound_file):
        self.location = sound_file
        self.sound = pygame.mixer.Sound(self.location)
        self.is_playing = False

    def play(self):
        if not self.is_playing:
            self.sound.play()
            self.is_playing = True
        self.is_playing = True
