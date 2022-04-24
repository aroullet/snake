from point import Point


class Grid:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.array = self.build_grid()

    def build_grid(self) -> list[list[Point]]:
        arr = []
        for i in range(self.length):
            arr.append(self.generate_row(i))
        return arr

    def generate_row(self, index: int):
        return [Point(x, index) for x in range(self.width)]

