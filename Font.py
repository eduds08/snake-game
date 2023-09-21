import pygame
from Constants import *


class Font:
    def __init__(self, text, position):
        # Initialize a font
        self.__font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)
        # Make a surface that contains a text (with the font that was just initialized in the previous line)
        self.text_surface = self.__font.render(text, True, WHITE, BLACK)
        # Set a rect and its position for the text_surface
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.topleft = position

    def update_text(self, text):
        # Update the text into the text surface (Called when the player_score improves, so we update the score text)
        self.text_surface = self.__font.render(text, True, WHITE, BLACK)
