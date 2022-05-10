import pygame
from src.point import Point
from collections import deque


class Square(pygame.sprite.Sprite):
    def __init__(self, size):
        super(Square, self).__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


class GUI:

    def __init__(self, width: int, height: int, num_squares: int, square_size: int):
        pygame.init()
        pygame.display.set_caption('Snake')

        self._width = width
        self._height = height
        self._square_size = square_size
        self.screen = pygame.display.set_mode((self._width, self._height))

        self._squares = [Square(self._square_size) for i in range(num_squares)]
        self._fruit_square = Square(self._square_size)

    def draw(self, positions: deque[Point], fruit: Point, count: int) -> None:
        for i, square in enumerate(self._squares):
            self.screen.blit(square.surf, (positions[i].x*self._square_size, positions[i].y*self._square_size))
        self.screen.blit(self._fruit_square.surf, (fruit.x*self._square_size, fruit.y*self._square_size))
        self._display_score(count)
        pygame.display.flip()

    def _display_score(self, count: int) -> None:
        font = pygame.font.SysFont('Roboto', 32)
        text = font.render(f'Score: {count}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(self._width/2, self._height/20))
        self.screen.blit(text, text_rect)

    def add_new_square(self) -> None:
        self._squares.append(Square(self._square_size))
