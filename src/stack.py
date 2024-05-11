from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None


class Stack(Generic[T]):
    def __init__(self):
        ...

    def push(self, value: T) -> None:
        ...

    def pop(self) -> Union[T, None]:
        ...

    def peek(self) -> Union[T, None]:
        ...

    def is_empty(self) -> bool:
        ...
