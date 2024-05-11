from typing import Union


class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.left: Union[Node, None] = None
        self.right: Union[Node, None] = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Union[Node, None] = None

    def insert(self, data: int) -> None:
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data: int, node: Node) -> None:
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def remove(self, data: int) -> None:
        self.root = self._remove(data, self.root)

    def _remove(self, data: int, node: Union[Node, None]) -> Union[Node, None]:
        if node is None:
            return None
        if data < node.data:
            node.left = self._remove(data, node.left)
        elif data > node.data:
            node.right = self._remove(data, node.right)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = node.right
            while temp.left is not None:
                temp = temp.left
            node.data = temp.data
            node.right = self._remove(temp.data, node.right)
        return node

    def search(self, data: int) -> bool:
        return self._search(data, self.root)

    def _search(self, data: int, node: Union[Node, None]) -> bool:
        if node is None:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._search(data, node.left)
        return self._search(data, node.right)

    def inorder(self) -> list[int]:
        return self._inorder(self.root)

    def _inorder(self, node: Union[Node, None]) -> list[int]:
        if node is None:
            return []
        return self._inorder(node.left) + [node.data] + self._inorder(node.right)

    def preorder(self) -> list[int]:
        return self._preorder(self.root)

    def _preorder(self, node: Union[Node, None]) -> list[int]:
        if node is None:
            return []
        return [node.data] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self) -> list[int]:
        return self._postorder(self.root)

    def _postorder(self, node: Union[Node, None]) -> list[int]:
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.data]

    def minimum(self) -> Union[int, None]:
        if self.root is None:
            return None

        node = self.root
        while node.left is not None:
            node = node.left

        return node.data

    def maximum(self) -> Union[int, None]:
        if self.root is None:
            return None
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data

    def height(self) -> int:
        return 1 + self._height(self.root)

    def _height(self, node: Union[Node, None]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self) -> int:
        return self._size(self.root)

    def _size(self, node: Union[Node, None]) -> int:
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)
