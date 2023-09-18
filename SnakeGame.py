import pygame
from pathlib import Path
import json
from Font import Font
from Snake import Snake
from Apple import Apple
from Constants import *


def render():
    # Draws all objects into the screen
    if snake_alive:
        screen.fill(BLACK)

        screen.blit(score_text.text_surface, score_text.text_rect)
        screen.blit(line_text.text_surface, line_text.text_rect)
        screen.blit(record_text.text_surface, record_text.text_rect)

        snake.draw_into_surface(screen, GREEN)
        apple.draw_into_surface(screen)
    else:
        screen.fill(BLACK)

        screen.blit(score_text.text_surface, score_text.text_rect)
        screen.blit(line_text.text_surface, line_text.text_rect)
        screen.blit(record_text.text_surface, record_text.text_rect)

        snake.draw_into_surface(screen, WHITE)


path = Path('data/score.json')

if path.exists():
    content = path.read_text()
    player_record_score = json.loads(content)
else:
    player_record_score = 0


### Control Flags ###
game_open = True
snake_alive = True
# The key_delay_flag acts as a "delay" for the input. Without this, if you press 2 keys very quick, only the 2nd input will happen
key_delay_flag = False
player_score = 0

### Initialize PYGAME, PYGAME.MIXER and the PYGAME'S CLOCK ###
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('sounds/eat_apple.wav')
clock = pygame.time.Clock()

### Instantiate game objects ###
snake = Snake()
apple = Apple()
score_text = Font(f'Score: {player_score}', SCORE_POSITION)
line_text = Font('-'*86, LINE_POSITION)
record_text = Font(f'Record: {player_record_score}', RECORD_POSITION)

### Create the screen (main surface) ###
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

# Main loop
while game_open and snake_alive:
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            game_open = False

        # Snake inputs
        elif event.type == pygame.KEYDOWN and not key_delay_flag:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.set_direction(UP)
            if event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.set_direction(RIGHT)
            if event.key == pygame.K_DOWN and snake.direction != UP:
                snake.set_direction(DOWN)
            if event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.set_direction(LEFT)
            key_delay_flag = not key_delay_flag

    if not game_open:
        break

    if key_delay_flag:
        key_delay_flag = not key_delay_flag

    # Moves the snake
    snake.move_head()

    # Checks if the snake ate the apple
    if snake.collide(apple.position):
        snake.increase_body()
        pygame.mixer.music.play()
        player_score += 1
        score_text.update_text(f'Score: {player_score}')
        apple.update_position()
        # This for loop makes sure that the new apple doesn't spawn on a position occupied by the snake
        for c in range(0, len(snake.body)):
            if apple.position == list(snake.body[c]):
                apple.update_position()
                c = 0

    # Checks if the snake is alive and also moves its body (excluding the head)
    snake_alive = snake.is_alive()

    # Draw stuff into the screen
    render()

    # Refresh the display
    pygame.display.flip()

    # Sets the game FPS
    clock.tick(FPS)

if not snake_alive:
    del apple

    if player_score > player_record_score:
        content = json.dumps(player_score)
        path.write_text(content)
        player_record_score = player_score

    render()

    pygame.mixer.music.load('sounds/game_over.wav')
    pygame.mixer.music.play()

    while game_open:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_open = False

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
