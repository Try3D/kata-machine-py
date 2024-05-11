from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None
        self.prev: Union[Node[T], None] = None


class Queue(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value: T) -> None:
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            if self.tail is not None:
                self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def dequeue(self) -> Union[T, None]:
        if self.head is None:
            return None
        elif self.head == self.tail:
            data = self.head.data
            self.head = self.tail = None
            return data
        else:
            data = self.head.data
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return data

    def peek(self) -> Union[T, None]:
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self) -> bool:
        return self.head is None
