import pygame
from point import Point


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

        self.width = width
        self.height = height
        self.square_size = square_size

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.topbar = pygame.Surface((self.width, self.height/20))

        self.squares = [Square(self.square_size) for i in range(num_squares)]
        self.fruit_square = Square(self.square_size)

    def draw(self, positions: list[Point], fruit: Point, count: int):
        for i, square in enumerate(self.squares):
            self.screen.blit(square.surf, (positions[i].x*self.square_size, positions[i].y*self.square_size))
        self.screen.blit(self.fruit_square.surf, (fruit.x*self.square_size, fruit.y*self.square_size))
        self.display_score(count)
        pygame.display.flip()

    def display_score(self, count: int):
        font = pygame.font.SysFont('Roboto', 32)
        text = font.render(f'Score: {count}', True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width/2, self.height/20))
        self.screen.blit(text, text_rect)

    def add_new_square(self):
        self.squares.append(Square(self.square_size))
