from grid import Grid
from snake import Snake
from point import Point


class SnakeGame:

    def __init__(self):
        self.grid = Grid(10, 10)
        self.snake = Snake(initial_pos=[Point(2, 4), Point(2, 3), Point(2, 2)])

    def run(self) -> None:
        for i in range(5):
            print(self.snake)
            print(f'Step {i}')
            self.render_grid()
            self.snake.update_position()
        self.snake.move_down()
        for j in range(3):
            print(self.snake)
            print(f'Step {j+5}')
            self.render_grid()
            self.snake.update_position()

    def render_grid(self):
        for row in self.grid.array:
            for point in row:
                if point in self.snake.position:
                    print('| x ', end='')
                else:
                    print(point, end='')
            print('|')
            print('----' * self.grid.width)

