from enum import Enum, auto
from collections import deque
from src.point import Point


class Directions(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


class Snake:

    def __init__(self, initial_pos: deque[Point]):
        self.position = initial_pos
        self._direction = Directions.RIGHT
        self._last_tail = None

    def __str__(self) -> str:
        return f'{self.position}'

    def update_position(self) -> None:
        """
        The position of the snake is updated by popping the tail and inserting a new head based on current direction.
        """
        self._last_tail = self.position[-1]  # Update old tail (used when growing snake)
        self.position.pop()  # Remove tail
        self._update_head()

    def _update_head(self) -> None:
        head = self.position[0]
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

        self.position.appendleft(Point(new_x, new_y))

    @property
    def length(self) -> int:
        return len(self.position)

    def grow(self) -> None:
        self.position.append(self._last_tail)

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
