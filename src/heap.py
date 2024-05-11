from typing import TypeVar, Union


T = TypeVar("T")


class Heap:
    def __init__(self):
        self.heap: list[int] = []

    def insert(self, value: int):
        ...

    def remove(self) -> Union[int, None]:
        ...

    def array(self) -> list[int]:
        ...
