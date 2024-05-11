from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None
        self.prev: Union[Node[T], None] = None


class Deque(Generic[T]):
    def __init__(self):
        ...

    def push_back(self, value: T) -> None:
        ...

    def push_front(self, value: T) -> None:
        ...

    def pop_back(self) -> Union[T, None]:
        ...

    def pop_front(self) -> Union[T, None]:
        ...

    def peek_back(self) -> Union[T, None]:
        ...

    def peek_front(self) -> Union[T, None]:
        ...

    def is_empty(self) -> bool:
        ...
