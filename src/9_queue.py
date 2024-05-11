from typing import TypeVar, Generic

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self):
        ...

    def enqueue(self, value: T) -> None:
        ...

    def dequeue(self) -> T:
        ...

    def peek(self) -> T:
        ...

    def is_empty(self) -> bool:
        ...
