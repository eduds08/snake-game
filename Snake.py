import pygame
from Constants import *


class Snake:
    def __init__(self, screen):
        # Set the first position of the snake and its direction
        self.body = [(SNAKE_FIRST_X_POSITION, SNAKE_FIRST_Y_POSITION), (SNAKE_FIRST_X_POSITION - OBJECT_SIZE, SNAKE_FIRST_Y_POSITION),
                     (SNAKE_FIRST_X_POSITION - OBJECT_SIZE * 2, SNAKE_FIRST_Y_POSITION)]
        
        #self.head_direction = RIGHT
        #self.previous_head_direction = RIGHT

        self.directions = [RIGHT, RIGHT, RIGHT]
        self.previous_directions = [RIGHT, RIGHT, RIGHT]

        self.screen = screen

        self.head_image = pygame.image.load('./snake_head.png').convert()
        self.body_image = pygame.image.load('./snake_body.png').convert()
        self.tail_image = pygame.image.load('./snake_tail.png').convert()

        self.head_image = pygame.transform.rotate(self.head_image, -90)

    def collide(self, apple):
        head = self.body[0]
        head_rect = pygame.rect.Rect(
            head[0], head[1], OBJECT_SIZE, OBJECT_SIZE)
        apple_rect = pygame.rect.Rect(
            apple[0], apple[1], OBJECT_SIZE, OBJECT_SIZE)
        return head_rect.colliderect(apple_rect)
    
    def update_image(self, img_name, pos):
        if self.directions[pos] == RIGHT:
            if self.previous_directions[pos] == UP:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, -90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, 90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, 90) 
            elif self.previous_directions[pos] == DOWN:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, 90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, -90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, -90)
        elif self.directions[pos] == LEFT:
            if self.previous_directions[pos] == UP:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, 90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, -90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, -90)
            elif self.previous_directions[pos] == DOWN:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, -90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, 90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, 90)
        elif self.directions[pos] == UP:
            if self.previous_directions[pos] == RIGHT:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, 90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, -90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, -90)
            elif self.previous_directions[pos] == LEFT:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, -90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, 90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, 90)
        elif self.directions[pos] == DOWN:
            if self.previous_directions[pos] == RIGHT:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, -90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, 90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, 90)
            elif self.previous_directions[pos] == LEFT:
                if img_name == 'HEAD':
                    self.head_image = pygame.transform.rotate(self.head_image, 90)
                if img_name == 'BODY':
                    self.body_image = pygame.transform.rotate(self.body_image, -90)
                if img_name == 'TAIL':
                    self.tail_image = pygame.transform.rotate(self.tail_image, -90)

    def set_direction(self, direction):
        # Just updates the snake's direction
        self.previous_directions[0] = self.directions[0]
        self.directions[0] = direction

        self.update_image('HEAD', 0)

        # if self.directions[0] == RIGHT:
        #     if self.previous_directions[0] == UP:
        #         self.head_image = pygame.transform.rotate(self.head_image, -90)
        #     elif self.previous_directions[0] == DOWN:
        #         self.head_image = pygame.transform.rotate(self.head_image, 90)
        # elif self.directions[0] == LEFT:
        #     if self.previous_directions[0] == UP:
        #         self.head_image = pygame.transform.rotate(self.head_image, 90)
        #     elif self.previous_directions[0] == DOWN:
        #         self.head_image = pygame.transform.rotate(self.head_image, -90)
        # elif self.directions[0] == UP:
        #     if self.previous_directions[0] == RIGHT:
        #         self.head_image = pygame.transform.rotate(self.head_image, 90)
        #     elif self.previous_directions[0] == LEFT:
        #         self.head_image = pygame.transform.rotate(self.head_image, -90)
        # elif self.directions[0] == DOWN:
        #     if self.previous_directions[0] == RIGHT:
        #         self.head_image = pygame.transform.rotate(self.head_image, -90)
        #     elif self.previous_directions[0] == LEFT:
        #         self.head_image = pygame.transform.rotate(self.head_image, 90)

    def move_head(self):
        # Moves the snake's head according to its direction
        if self.directions[0] == UP:
            self.body[0] = (self.body[0][0], self.body[0][1] - OBJECT_SIZE)
        if self.directions[0] == RIGHT:
            self.body[0] = (self.body[0][0] + OBJECT_SIZE, self.body[0][1])
        if self.directions[0] == DOWN:
            self.body[0] = (self.body[0][0], self.body[0][1] + OBJECT_SIZE)
        if self.directions[0] == LEFT:
            self.body[0] = (self.body[0][0] - OBJECT_SIZE, self.body[0][1])

    def move_body(self, current_position, previous_position):

        self.previous_directions[current_position] = self.directions[current_position]
        self.directions[current_position] = self.directions[previous_position]

        self.body[current_position] = self.body[previous_position]

    def move_body_aux(self):

        for c in range(len(self.body) - 1, 0, -1):
            self.move_body(c, c-1)

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
            # Also moves the body (so we don't need to make another for-loop just for it)

        # If it runs this line, the snake is still alive
        return True

    def increase_body(self):
        # Add 1 position to the body when the snake eats an apple
        self.body.append((self.body[-1][0], self.body[-1][1]))
        self.directions.append(RIGHT)
        self.previous_directions.append(RIGHT)

    def blitme(self):

        head_rect = pygame.Rect(
            self.body[0][0], self.body[0][1], OBJECT_SIZE, OBJECT_SIZE)
        self.screen.blit(self.head_image, head_rect)

        for c in range(1, len(self.body) - 1):
            self.update_image('BODY', c)
            body_rect = pygame.Rect(
                self.body[c][0], self.body[c][1], OBJECT_SIZE, OBJECT_SIZE)
            self.screen.blit(self.body_image, body_rect)

        self.update_image('TAIL', -1)
        tail_rect = pygame.Rect(
            self.body[-1][0], self.body[-1][1], OBJECT_SIZE, OBJECT_SIZE)
        self.screen.blit(self.tail_image, tail_rect)
