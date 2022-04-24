import pygame
from point import Point

BLOCK_SIZE = 25


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()

        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))

        # Define the color of the surface using RGB color coding.
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


class GUI:

    def __init__(self, num_squares):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.squares = [Square() for i in range(num_squares)]

    def draw(self, positions: list[Point]):
        for i, square in enumerate(self.squares):
            self.screen.blit(square.surf, (positions[i].x*BLOCK_SIZE, positions[i].y*BLOCK_SIZE))
        pygame.display.flip()
