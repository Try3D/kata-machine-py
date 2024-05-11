from typing import TypeVar, Generic

T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self):
        ...

    def insbeg(self, value: T) -> None:
        ...

    def insend(self, value: T) -> None:
        ...

    def inspos(self, index: int, value: T) -> None:
        ...

    def delbeg(self) -> None:
        ...

    def delend(self) -> None:
        ...

    def delpos(self) -> None:
        ...

    def rem(self, value: T) -> None:
        ...

    def display(self):
        ...

    def display_reverse(self):
        ...

    def reverse(self):
        ...
