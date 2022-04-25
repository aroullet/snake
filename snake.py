from enum import Enum, auto
from point import Point


class Directions(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Snake:

    def __init__(self, initial_pos: list[Point] = [Point(i, 20) for i in range(5)]):
        self.position = initial_pos
        self._direction = Directions.RIGHT
        self._last_pos = None

    def __str__(self) -> str:
        return f'{self.position}'

    def update_position(self) -> None:
        """
        Iterates over position array from tail to head, setting position of block i to that of block i+1
        """
        self._last_pos = self.position[0]
        for i in range(self.length-1):
            self.position[i] = self.position[i+1]
        self._update_head()

    def _update_head(self) -> None:
        head = self.position[-1]
        new_x, new_y = head.x, head.y

        # Origin is in top-left corner, therefore increasing values of y go down
        if self._direction == Directions.UP:
            new_y -= 1

        elif self._direction == Directions.DOWN:
            new_y += 1

        elif self._direction == Directions.RIGHT:
            new_x += 1

        elif self._direction == Directions.LEFT:
            new_x -= 1

        self.position[-1] = Point(new_x, new_y)

    @property
    def length(self) -> int:
        return len(self.position)

    def grow(self) -> None:
        self.position.insert(0, self._last_pos)

    def move_up(self) -> None:
        if self._direction != Directions.DOWN:
            self._direction = Directions.UP

    def move_down(self) -> None:
        if self._direction != Directions.UP:
            self._direction = Directions.DOWN

    def move_left(self) -> None:
        if self._direction != Directions.RIGHT:
            self._direction = Directions.LEFT

    def move_right(self) -> None:
        if self._direction != Directions.LEFT:
            self._direction = Directions.RIGHT
