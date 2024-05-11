from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None


class Stack(Generic[T]):
    def __init__(self):
        self.head = None

    def push(self, value: T) -> None:
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def pop(self) -> Union[T, None]:
        if self.head is None:
            return None
        else:
            value = self.head.data
            self.head = self.head.next
            return value

    def peek(self) -> Union[T, None]:
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self) -> bool:
        return self.head is None
