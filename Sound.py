import pygame


class Sound:
    """Create the Sound for the game. If music is not playing, play music.

        Attributes:
            location (Any): Location of the sound file
            sound (Sound): Sound.
            is_playing (bool): Checks if the sound is playing.

    """

    def __init__(self, sound_file):
        """Holds parameters and attributes of the Sound class.

        :param sound_file: Sound-file.

        """
        self.location = sound_file
        self.sound = pygame.mixer.Sound(self.location)
        self.is_playing = False

    def play(self):
        """If the music is not playing, play the music.

        :param -> None
        :return -> None

        """
        if not self.is_playing:
            self.sound.play()
            self.is_playing = True
        self.is_playing = True
