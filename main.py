import pygame
from pathlib import Path
import json
from Font import Font
from Snake import Snake
from Apple import Apple
from Constants import *


def render():
    # Draws all objects into the screen
    screen.fill(BLACK)

    score_text.render()
    line_text.render()
    record_text.render()

    if snake_alive:
        snake.render()
        apple.render()
    # else:
        # snake.draw_into_surface(screen, WHITE)


path = Path('data')


if path.exists():
    path = Path('data/score.json')
    content = path.read_text()
    player_record_score = json.loads(content)
else:
    player_record_score = 0
    path.mkdir()
    path = Path('data/score.json')

### Control Flags ###
game_open = True
snake_alive = True
# The key_delay_flag acts as a "delay" for the input. Without this, if you press 2 keys very quick, only the 2nd input will happen
#key_delay_flag = False
# player_score = 0

### Initialize PYGAME, PYGAME.MIXER and the PYGAME'S CLOCK ###
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('sounds/eat_apple.wav')
clock = pygame.time.Clock()

### Create the screen (main surface) ###
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Snake Game")

### Instantiate game objects ###
snake = Snake(screen)
apple = Apple(screen)
score_text = Font(f'Score: {snake.score}', SCORE_POSITION, screen)
line_text = Font('-'*86, LINE_POSITION, screen)
record_text = Font(f'Record: {player_record_score}', RECORD_POSITION, screen)


# Main loop
while game_open and snake_alive:
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            game_open = False

    if not game_open:
        break

    snake.update(apple)

    score_text.update(f'Score: {snake.score}')

    snake_alive = snake.is_alive

    # Draw stuff into the screen
    render()

    # Refresh the display
    pygame.display.flip()

    # Sets the game FPS
    clock.tick(FPS)

if not snake_alive:
    del apple

    if snake.score > player_record_score or player_record_score == 0:
        content = json.dumps(snake.score)
        path.write_text(content)
        player_record_score = snake.score

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
