import pygame
from random import randint
from Constants import *


class Apple:
    def __init__(self, screen):
        self.__screen = screen
        self.__position = self.__generate_random_position()

    def update(self):
        self.__position = self.__generate_random_position()

    def render(self):
        apple_rect = pygame.Rect(
            self.__position[0], self.__position[1], OBJECT_SIZE, OBJECT_SIZE)
        pygame.draw.rect(self.__screen, RED, apple_rect)

    @property
    def position(self):
        return self.__position

    def __generate_random_position(self):
        # Generates a random position for the apple (valid position constrained to the screen borders)
        new_position = [randint(0, SCREEN_SIZE - OBJECT_SIZE),
                        randint(SCREEN_BEGIN_Y, SCREEN_SIZE - OBJECT_SIZE)]

        # Rounds the new_position value to be a product of 10 (10, 20, 30, 40, 50...)
        new_position[0] = new_position[0] // 10 * 10
        new_position[1] = new_position[1] // 10 * 10

        # Updates the x-coord and y-coord until both becomes a product of 32 (32, 64, 96) --- 32 is the object_size
        while new_position[0] % OBJECT_SIZE != 0:
            new_position[0] += 2
        while new_position[1] % OBJECT_SIZE != 0:
            new_position[1] += 2

        new_position_tuple = (new_position[0], new_position[1])

        return new_position_tuple
