import pygame
from random import randint
from Constants import *


class Apple:
    def __init__(self):
        self.position = self.generate_random_position()

    def generate_random_position(self):
        # Generates a random position for the apple (valid position constrained to the screen borders)
        new_position = [randint(0, SCREEN_SIZE - OBJECT_SIZE),
                        randint(SCREEN_BEGIN_Y, SCREEN_SIZE - OBJECT_SIZE)]

        # Rounds the new_position value to be a product of 10 (10, 20, 30, 40, 50...)
        new_position[0] = new_position[0] // 10 * 10
        new_position[1] = new_position[1] // 10 * 10

        # Updates the x-coord and y-coord until both becomes a product of 20 (20, 40, 60) --- 20 is the object_size
        while new_position[0] % OBJECT_SIZE != 0:
            new_position[0] += 1
        while new_position[1] % OBJECT_SIZE != 0:
            new_position[1] += 1

        return new_position

    def update_position(self):
        # Called when the snake eats an apple
        self.position = self.generate_random_position()

    def draw_into_surface(self, surface):
        # Make the apple a pygame rect and draw into the surface (the surface is the main screen)
        apple_skin = pygame.Rect(
            self.position[0], self.position[1], OBJECT_SIZE, OBJECT_SIZE)
        pygame.draw.rect(surface, RED, apple_skin)
