# import pygame
# from pathlib import Path
# import json
# from Font import Font
# from Snake import Snake
# from Apple import Apple
# from Constants import *


# class SnakeGame:
#     def __init__(self):
#         self.path = Path('data')

#         if path.exists():
#             path = Path('data/score.json')
#             content = path.read_text()
#             self.player_record_score = json.loads(content)
#         else:
#             self.player_record_score = 0
#             path.mkdir()
#             path = Path('data/score.json')

#         ### Control Flags ###
#         self.game_open = True
#         self.snake_alive = True
#         # The key_delay_flag acts as a "delay" for the input. Without this, if you press 2 keys very quick, only the 2nd input will happen
#         self.key_delay_flag = False
#         self.player_score = 0

#         self.clock = pygame.time.Clock()

#         ### Instantiate game objects ###
#         self.snake = Snake()
#         self.apple = Apple()
#         self.score_text = Font(f'Score: {self.player_score}', SCORE_POSITION)
#         self.line_text = Font('-'*86, LINE_POSITION)
#         self.record_text = Font(
#             f'Record: {self.player_record_score}', RECORD_POSITION)

#         ### Create the screen (main surface) ###
#         self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
#         pygame.display.set_caption("Snake Game")

#     def render(self):
#         # Draws all objects into the screen
#         self.screen.fill(BLACK)

#         self.screen.blit(self.score_text.text_surface,
#                          self.score_text.text_rect)
#         self.screen.blit(self.line_text.text_surface, self.line_text.text_rect)
#         self.screen.blit(self.record_text.text_surface,
#                          self.record_text.text_rect)

#         if self.snake_alive:
#             self.snake.draw_into_surface(self.screen, GREEN)
#             self.apple.draw_into_surface(self.screen)
#         else:
#             self.snake.draw_into_surface(self.screen, WHITE)
