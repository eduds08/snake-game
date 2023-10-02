import pygame
from Constants import *


class Snake:
    def __init__(self, screen):
        # Set the first position of the snake and its direction
        self.__body = [(SNAKE_FIRST_X_POSITION, SNAKE_FIRST_Y_POSITION), (SNAKE_FIRST_X_POSITION - OBJECT_SIZE, SNAKE_FIRST_Y_POSITION),
                     (SNAKE_FIRST_X_POSITION - OBJECT_SIZE * 2, SNAKE_FIRST_Y_POSITION)]
        self.__head_direction = RIGHT
        self.__screen = screen

        self.__is_alive = True

        self.__score = 0

        self.collided = False

        self.key_delay_flag = False

    @property
    def body(self):
        return self.__body
    
    @property
    def is_alive(self):
        return self.__is_alive
    
    @property
    def score(self):
        return self.__score

    def update(self, apple):
        self.__update_movement()
        self.__update_collision(apple)
        self.__update_is_alive()

    def __update_movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.__head_direction != DOWN:
            self.__head_direction = UP
        if keys[pygame.K_RIGHT] and self.__head_direction != LEFT:
            self.__head_direction = RIGHT
        if keys[pygame.K_DOWN] and self.__head_direction != UP:
            self.__head_direction = DOWN
        if keys[pygame.K_LEFT] and self.__head_direction != RIGHT:
            self.__head_direction = LEFT

        for c in range(len(self.__body) -1, 0, -1):
            self.__body[c] = self.__body[c-1]

        if self.__head_direction == UP:
            self.__body[0] = (self.__body[0][0], self.__body[0][1] - OBJECT_SIZE)
        if self.__head_direction == RIGHT:
            self.__body[0] = (self.__body[0][0] + OBJECT_SIZE, self.__body[0][1])
        if self.__head_direction == DOWN:
            self.__body[0] = (self.__body[0][0], self.__body[0][1] + OBJECT_SIZE)
        if self.__head_direction == LEFT:
            self.__body[0] = (self.__body[0][0] - OBJECT_SIZE, self.__body[0][1])

    def __update_collision(self, apple):
        head = self.__body[0]
        head_rect = pygame.rect.Rect(
            head[0], head[1], OBJECT_SIZE, OBJECT_SIZE)
        apple_rect = pygame.rect.Rect(
            apple.position[0], apple.position[1], OBJECT_SIZE, OBJECT_SIZE)

        if head_rect.colliderect(apple_rect):
            self.collided = True
        else:
            self.collided = False

        if (self.collided):
            self.__increase_body()
            pygame.mixer.music.play()
            self.__score += 1
            apple.update()
            for c in range(0, len(self.__body)):
                if apple.position == self.__body[c]:
                    apple.update()
                    c = 0

    def __update_is_alive(self):
        # Snake's head (First list position)
        snake_head = self.__body[0]

        # Checks if the snake's head hit the screen borders (top border is the dashed line -> "---")
        if snake_head[0] < 0 or snake_head[0] > SCREEN_SIZE - OBJECT_SIZE or snake_head[1] < SCREEN_BEGIN_Y or snake_head[1] > SCREEN_SIZE - OBJECT_SIZE:
            self.__is_alive = False

        # Iterates over the whole body, excluding the head
        for c in range(len(self.__body) - 1, 0, -1):
            # Check if the snake's head hit its body
            if snake_head == self.__body[c]:
                self.__is_alive = False
            # Also moves the body (so we don't need to make another for-loop just for it)

    def __increase_body(self):
        # Add 1 position to the body when the snake eats an apple
        self.__body.append((self.__body[-1][0], self.__body[-1][1]))

    def render(self):
        for body_rect in self.__body:
            rect = pygame.Rect(body_rect[0], body_rect[1], OBJECT_SIZE, OBJECT_SIZE)
            pygame.draw.rect(self.__screen, GREEN, rect)
