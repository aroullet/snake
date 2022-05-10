import os
from random import randint
from collections import deque
import pygame
from pygame.locals import *

from config import read_config
from src.snake import Snake
from src.point import Point
from src.gui import GUI

cfg = read_config(os.path.join(os.path.dirname(__file__), '../config.json'))


class SnakeGame:

    def __init__(self):
        # Center the snake vertically when the game starts, initializes it with 5 squares
        self.snake = Snake(initial_pos=deque([Point(i, cfg.height//(2*cfg.square_size)) for i in range(5, 0, -1)]))
        self.fruit = SnakeGame._random_fruit()
        self.score = 0

        self.gui = GUI(width=cfg.width, height=cfg.height, num_squares=self.snake.length, square_size=cfg.square_size)
        self.running = True
        self.paused = False
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

    def pause_game(self):
        while self.paused:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_p:
                    self.paused = False

    def _check_fruit(self) -> None:
        if self.snake.position[-1] == self.fruit:
            self.snake.grow()
            self.fruit = SnakeGame._random_fruit()
            self.gui.add_new_square()
            self.score += 1

    def _check_out_of_bounds(self) -> None:
        head = self.snake.position[0]
        if not (0 < head.x < cfg.width/cfg.square_size):
            self.running = False
            print('You ran into a wall!')

        elif not (0 < head.y < cfg.height/cfg.square_size):
            self.running = False
            print('You ran into a wall!')

    def _check_collision(self) -> None:
        if len(set(self.snake.position)) < self.snake.length:  # check for duplicate points in positions list
            self.running = False
            print('You hit yourself!')

    def _check_events(self) -> None:
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

                elif event.key == K_p:
                    self.paused = True
                    self.pause_game()

            elif event.type == QUIT:
                self.running = False

    @staticmethod
    def _random_fruit() -> Point:
        return Point(randint(0, cfg.width)//cfg.square_size, randint(0, cfg.height)//cfg.square_size)
