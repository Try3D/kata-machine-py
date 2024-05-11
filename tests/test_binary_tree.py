from exercises.binary_tree import BinaryTree


def test_binary_tree_insert_and_search():
    # Create a binary tree
    binary_tree = BinaryTree()

    # Insert some elements
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    # Test search for existing and non-existing elements
    assert binary_tree.search(5) == True
    assert binary_tree.search(3) == True
    assert binary_tree.search(8) == True
    assert binary_tree.search(1) == True
    assert binary_tree.search(4) == True
    assert binary_tree.search(7) == True
    assert binary_tree.search(9) == True
    assert binary_tree.search(0) == False
    assert binary_tree.search(2) == False
    assert binary_tree.search(6) == False
    assert binary_tree.search(10) == False


def test_binary_tree_inorder_traversal():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.inorder() == [1, 3, 4, 5, 7, 8, 9]


def test_binary_tree_preorder_traversal():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.preorder() == [5, 3, 1, 4, 8, 7, 9]


def test_binary_tree_postorder_traversal():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.postorder() == [1, 4, 3, 7, 9, 8, 5]


def test_binary_tree_minimum():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.minimum() == 1


def test_binary_tree_maximum():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.maximum() == 9


def test_binary_tree_height():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.height() == 3


def test_binary_tree_size():
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(1)
    binary_tree.insert(4)
    binary_tree.insert(7)
    binary_tree.insert(9)

    assert binary_tree.size() == 7
