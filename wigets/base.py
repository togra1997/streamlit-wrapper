from dataclasses import dataclass


@dataclass
class StreamBase:
    def __post_init__(self):
        self.set_wiget()

    def set_wiget(self):
        pass
