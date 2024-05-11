from exercises.queue import Queue


def test_queue_enqueue():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1


def test_queue_dequeue():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1


def test_queue_peek():
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.peek() == 1


def test_queue_is_empty():
    queue = Queue[int]()
    assert queue.is_empty() == True

    queue.enqueue(1)
    assert queue.is_empty() == False

    queue.dequeue()
    assert queue.is_empty() == True
