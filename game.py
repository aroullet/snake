import os
from random import randint
import pygame
from pygame.locals import *

from config import read_config
from snake import Snake
from point import Point
from gui import GUI

cfg = read_config(os.path.join(os.path.dirname(__file__), 'config.json'))


class SnakeGame:

    def __init__(self):
        self.snake = Snake()
        self.fruit = SnakeGame._random_fruit()
        self.score = 0

        self.gui = GUI(width=cfg.width, height=cfg.height, num_squares=self.snake.length, square_size=cfg.square_size)
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while self.running:
            self.gui.screen.fill((0, 0, 0))  # Clear screen
            self._check_events()
            self.snake.update_position()

            self.gui.draw(self.snake.position, self.fruit, self.score)
            self._check_out_of_bounds()
            self._check_collision()
            self._check_fruit()

            self.clock.tick(60)  # 60 loops per second to ensure fast key events are properly handled
            pygame.time.delay(cfg.refresh_delay)

        pygame.display.quit()
        pygame.quit()
        quit(0)

    def _check_fruit(self):
        if self.snake.position[-1] == self.fruit:
            self.snake.grow()
            self.fruit = SnakeGame._random_fruit()
            self.gui.add_new_square()
            self.score += 1

    def _check_out_of_bounds(self):
        head = self.snake.position[-1]
        if not (0 < head.x < cfg.width/cfg.square_size):
            self.running = False
            print('You ran into a wall!')

        elif not (0 < head.y < cfg.height/cfg.square_size):
            self.running = False
            print('You ran into a wall!')

    def _check_collision(self):
        if len(set(self.snake.position)) < self.snake.length:  # _check for duplicate points in positions list
            self.running = False
            print('You hit yourself!')

    def _check_events(self):
        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    self.snake.move_up()

                elif event.key == K_DOWN:
                    self.snake.move_down()

                elif event.key == K_LEFT:
                    self.snake.move_left()

                elif event.key == K_RIGHT:
                    self.snake.move_right()

            elif event.type == QUIT:
                self.running = False

    @staticmethod
    def _random_fruit():
        return Point(randint(0, cfg.width)//cfg.square_size, randint(0, cfg.height)//cfg.square_size)
