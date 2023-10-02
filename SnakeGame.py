import pygame
from pathlib import Path
import json
from Font import Font
from Snake import Snake
from Apple import Apple
from Constants import *


class SnakeGame:
    def __init__(self):
        self.__game_open = True

        self.__init_path()
        self.__init_pygame()

        self.__screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        pygame.display.set_caption("Snake Game")
        
        self.__init_game_objects()

        self.__run()

        pygame.quit()

    def __init_path(self):
        if not Path('data').exists():
            Path('data').mkdir()
            Path('data/score.json').touch()
            Path('data/score.json').write_text('0')
        else:
            if not Path('data/score.json').exists():
                Path('data/score.json').touch()
                Path('data/score.json').write_text('0')

        self.__path = Path('data/score.json')
        self.__player_high_score = json.loads(self.__path.read_text())

    def __init_pygame(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load('sounds/eat_apple.wav')
        self.__clock = pygame.time.Clock()

    def __init_game_objects(self):
        self.__snake = Snake(self.__screen)
        self.__apple = Apple(self.__screen)
        self.__score_text = Font(f'Score: {self.__snake.score}', SCORE_POSITION, self.__screen)
        self.__line_text = Font('-'*86, LINE_POSITION, self.__screen)
        self.__record_text = Font(f'Record: {self.__player_high_score}', RECORD_POSITION, self.__screen)

    def __run(self):
        while self.__game_open and self.__snake.is_alive:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__game_open = False

            self.__update()
            self.__render()
            
            self.__clock.tick(FPS)

        if not self.__snake.is_alive:
            if self.__snake.score > self.__player_high_score:
                self.__path.write_text(json.dumps(self.__snake.score))
                self.__player_high_score = self.__snake.score

            self.__render()

            pygame.mixer.music.load('sounds/game_over.wav')
            pygame.mixer.music.play()

            while self.__game_open:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.__game_open = False
    
    def __render(self):
        self.__screen.fill(BLACK)

        self.__score_text.render()
        self.__line_text.render()
        self.__record_text.render()

        if self.__snake.is_alive:
            self.__snake.render()
            self.__apple.render()

        pygame.display.flip()

    def __update(self):
        self.__snake.update(self.__apple)
        self.__score_text.update(f'Score: {self.__snake.score}')
