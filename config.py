from dataclasses import dataclass
import json


@dataclass(frozen=True)
class GameConfig:
    width: int
    height: int
    square_size: int
    refresh_delay: int


def read_config(config_file: str) -> GameConfig:
    with open(config_file, 'r') as file:
        data = json.load(file)
        return GameConfig(**data)
