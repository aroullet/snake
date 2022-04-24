from snake import Snake
from point import Point
from gui import GUI
import pygame
from pygame.locals import *
from time import sleep


class SnakeGame:

    def __init__(self):
        self.snake = Snake(initial_pos=[Point(i, 20) for i in range(15)])
        self.gui = GUI(width=800, length=600, num_squares=self.snake.length)
        self.running = True

    def run(self) -> None:
        while self.running:
            self.gui.screen.fill((0, 0, 0))  # Clear screen
            self.check_events()
            self.gui.draw(self.snake.position)
            self.snake.update_position()
            self.check_out_of_bounds()
            self.check_collision()
            sleep(0.07)

    def check_out_of_bounds(self):
        for point in self.snake.position:
            if point.x < 0 or point.x > self.gui.width/15:
                self.running = False

            if point.y < 0 or point.y > self.gui.length/15:
                self.running = False

    def check_collision(self):
        if len(set(self.snake.position)) < self.snake.length:  # Check for duplicate points in positions list
            self.running = False

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

