import pygame
from Constants import *


class Font:
    def __init__(self, text, position, screen):
        # Initialize a font
        self.__font = pygame.font.Font('freesansbold.ttf', FONT_SIZE)

        self.__screen = screen
        # Make a surface that contains a text (with the font that was just initialized in the previous line)
        self.__text_surface = self.__font.render(text, True, WHITE, BLACK)
        # Set a rect and its position for the text_surface
        self.__text_rect = self.__text_surface.get_rect()
        self.__text_rect.topleft = position

    def update(self, text):
        # Update the text into the text surface (Called when the player_score improves, so we update the score text)
        self.__text_surface = self.__font.render(text, True, WHITE, BLACK)

    def render(self):
        self.__screen.blit(self.__text_surface, self.__text_rect)
