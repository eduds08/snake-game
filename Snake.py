import pygame
from Constants import *


class Snake:
    def __init__(self):
        # Set the first position of the snake and its direction
        self.body = [(SNAKE_FIRST_X_POSITION, SNAKE_FIRST_Y_POSITION), (SNAKE_FIRST_X_POSITION - OBJECT_SIZE, SNAKE_FIRST_Y_POSITION),
                     (SNAKE_FIRST_X_POSITION - OBJECT_SIZE * 2, SNAKE_FIRST_Y_POSITION)]
        self.direction = RIGHT

    def collide(self, apple):
        head = self.body[0]
        head_rect = pygame.rect.Rect(
            head[0], head[1], OBJECT_SIZE, OBJECT_SIZE)
        apple_rect = pygame.rect.Rect(
            apple[0], apple[1], OBJECT_SIZE, OBJECT_SIZE)
        return head_rect.colliderect(apple_rect)

    def set_direction(self, direction):
        # Just updates the snake's direction
        self.direction = direction

    def move_head(self):
        # Moves the snake's head according to its direction
        if self.direction == UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - OBJECT_SIZE)
        if self.direction == RIGHT:
            self.body[0] = (self.body[0][0] + OBJECT_SIZE, self.body[0][1])
        if self.direction == DOWN:
            self.body[0] = (self.body[0][0], self.body[0][1] + OBJECT_SIZE)
        if self.direction == LEFT:
            self.body[0] = (self.body[0][0] - OBJECT_SIZE, self.body[0][1])

    def move_body(self, current_position, previous_position):
        # Set each body position to the previous one (eg.: body[4] is set to the position of body[3])
        self.body[current_position] = self.body[previous_position]

    def is_alive(self):
        # Snake's head (First list position)
        head = self.body[0]

        # Checks if the snake's head hit the screen borders (top border is the dashed line -> "---")
        if head[0] < 0 or head[0] > SCREEN_SIZE - OBJECT_SIZE or head[1] < SCREEN_BEGIN_Y or head[1] > SCREEN_SIZE - OBJECT_SIZE:
            return False

        # Iterates over the whole body, excluding the head
        for c in range(len(self.body) - 1, 0, -1):
            # Check if the snake's head hit its body
            if head == self.body[c]:
                return False
            # Also moves the body (so we don't need to make another for loop just for it)
            self.move_body(c, c-1)

        # If it runs this line, the snake is still alive
        return True

    def draw_into_surface(self, surface, color):
        # Iterates over all snake body (including head)
        for square in self.body:
            # Make each body position a pygame rect
            snake_body = pygame.Rect(
                square[0], square[1], OBJECT_SIZE, OBJECT_SIZE)
            # Draw the rect into the surface (in this case, the surface is the main screen)
            pygame.draw.rect(surface, color, snake_body)

    def increase_body(self):
        # Add 1 position to the body when the snake eats an apple
        self.body.append((0, 0))
