import pygame
from random import randint
from Constants import *


class Apple:
    def __init__(self, screen):
        self.__screen = screen
        self.__image = pygame.image.load('./apple.png').convert()
        self.position = self.__generate_random_position()

    def update(self):
        self.position = self.__generate_random_position()

    def render(self):
        apple_rect = pygame.Rect(
            self.position[0], self.position[1], OBJECT_SIZE, OBJECT_SIZE)
        self.__screen.blit(self.__image, apple_rect)

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

        return new_position
