from dataclasses import dataclass
import json


@dataclass
class GameConfig:
    width: int
    height: int
    square_size: int
    refresh_delay: float


def read_config(config_file: str) -> GameConfig:
    with open(config_file, 'r') as file:
        data = json.load(file)
        return GameConfig(**data)
