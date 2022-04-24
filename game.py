from grid import Grid
from snake import Snake
from point import Point
from gui import GUI
import pygame
from pygame.locals import *
from time import sleep


class SnakeGame:

    def __init__(self):
        self.grid = Grid(10, 10)
        self.snake = Snake(initial_pos=[Point(2, 4), Point(2, 3), Point(2, 2)])
        self.gui = GUI(self.snake.length)
        self.running = True

    def run(self) -> None:
        while self.running:
            self.gui.screen.fill((0, 0, 0))  # Clear screen
            self.check_events()
            self.gui.draw(self.snake.position)
            self.snake.update_position()
            sleep(0.03)

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

