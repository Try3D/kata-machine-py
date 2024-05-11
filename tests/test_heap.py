from exercises.heap import Heap


def test_heap_insert():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    assert heap.array() == [8, 3, 5, 1]


def test_heap_remove():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    assert heap.remove() == 8
    assert heap.array() == [5, 3, 1]


def test_heap_array():
    heap = Heap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    assert heap.array() == [8, 3, 5, 1]
