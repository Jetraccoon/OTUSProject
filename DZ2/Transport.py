from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


class Transport(metaclass=ABCMeta):
    weight: int
    lifting: int

    @abstractmethod
    def make_sound(self):
        raise NotImplemented


@dataclass
class Engine:
    capacity: int
    power: int
    count_pistons: int

    def start_engine(self):
        print("Engine started!")
