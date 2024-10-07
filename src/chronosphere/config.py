from box import Box
from pathlib import Path

config = Box.from_toml(filename=Path(__file__).parent / "config.toml")
