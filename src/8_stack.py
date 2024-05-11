from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        ...

    def push(self, value: T) -> None:
        ...

    def pop(self) -> T:
        ...

    def peek(self) -> T:
        ...

    def is_empty(self) -> bool:
        ...
