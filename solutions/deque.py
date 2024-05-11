from typing import TypeVar, Generic, Union

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Union[Node[T], None] = None
        self.prev: Union[Node[T], None] = None


class Deque(Generic[T]):
    def __init__(self):
        self.head: Union[Node[T], None] = None
        self.tail: Union[Node[T], None] = None

    def push_back(self, value: T) -> None:
        if self.tail is None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def push_front(self, value: T) -> None:
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop_back(self) -> Union[T, None]:
        if self.tail is None:
            return None
        tmp = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return tmp

    def pop_front(self) -> Union[T, None]:
        if self.head is None:
            return None
        tmp = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return tmp

    def peek_back(self) -> Union[T, None]:
        if self.tail is None:
            return None
        else:
            return self.tail.data

    def peek_front(self) -> Union[T, None]:
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self) -> bool:
        return self.head is None
