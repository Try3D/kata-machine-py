from typing import Union


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None


class BinaryTree:
    def __init__(self) -> None:
        ...

    def insert(self, data: int) -> None:
        ...

    def remove(self, data: int) -> None:
        ...

    def search(self, data: int) -> bool:
        ...

    def inorder(self) -> list[int]:
        ...

    def preorder(self) -> list[int]:
        ...

    def postorder(self) -> list[int]:
        ...

    def minimum(self) -> Union[int, None]:
        ...

    def maximum(self) -> Union[int, None]:
        ...

    def height(self) -> int:
        ...

    def size(self) -> int:
        ...
