from point import Point


class Grid:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width
        self.array = self.build_grid()

    def build_grid(self) -> list[list[Point]]:
        arr = []
        for i in range(self._length):
            arr.append(self.generate_row(i))
        return arr

    def generate_row(self, index: int):
        return [Point(x, index) for x in range(self._width)]

    def print_grid(self):
        for row in self.array:
            print(row)


if __name__ == '__main__':
    grid = Grid(5, 5)
    print(grid)
