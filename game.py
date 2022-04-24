import pygame
from pygame.locals import *
from time import sleep
from random import randint
from config import read_config

from snake import Snake
from point import Point
from gui import GUI

cfg = read_config('./config.json')


class SnakeGame:

    def __init__(self):
        self.snake = Snake(initial_pos=[Point(i, 20) for i in range(10)])
        self.fruit = SnakeGame.random_fruit()

        self.gui = GUI(width=cfg.width, height=cfg.height, num_squares=self.snake.length, square_size=cfg.square_size)
        self.running = True

    def run(self) -> None:
        while self.running:
            self.gui.screen.fill((0, 0, 0))  # Clear screen
            self.check_events()
            self.gui.draw(self.snake.position, self.fruit)
            self.snake.update_position()
            self.check_fruit()
            self.check_out_of_bounds()
            self.check_collision()
            sleep(cfg.refresh_delay)

        pygame.display.quit()
        pygame.quit()
        quit(0)

    def check_fruit(self):
        if self.snake.position[-1] == self.fruit:
            self.snake.grow()
            self.fruit = SnakeGame.random_fruit()
            self.gui.add_new_square()

    def check_out_of_bounds(self):
        for point in self.snake.position:
            if point.x < 0 or point.x > cfg.width/cfg.square_size:
                self.running = False
                print('You ran into a wall!')

            if point.y < 0 or point.y > cfg.height/cfg.square_size:
                self.running = False
                print('You ran into a wall!')

    def check_collision(self):
        if len(set(self.snake.position)) < self.snake.length:  # Check for duplicate points in positions list
            self.running = False
            print('You hit yourself!')

    def check_events(self):
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
    def random_fruit():
        return Point(randint(0, cfg.width)//cfg.square_size, randint(0, cfg.height)//cfg.square_size)
