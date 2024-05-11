from exercises.deque import Deque


def test_deque_push_back():
    deque = Deque[int]()
    deque.push_back(1)
    deque.push_back(2)
    assert deque.peek_back() == 2


def test_deque_push_front():
    deque = Deque[int]()
    deque.push_front(1)
    deque.push_front(2)
    assert deque.peek_front() == 2


def test_deque_pop_back():
    deque = Deque[int]()
    deque.push_back(1)
    deque.push_back(2)
    assert deque.pop_back() == 2


def test_deque_pop_front():
    deque = Deque[int]()
    deque.push_back(1)
    deque.push_back(2)
    assert deque.pop_front() == 1


def test_deque_peek_back():
    deque = Deque[int]()
    deque.push_back(1)
    deque.push_back(2)
    assert deque.peek_back() == 2


def test_deque_peek_front():
    deque = Deque[int]()
    deque.push_back(1)
    deque.push_back(2)
    assert deque.peek_front() == 1


def test_deque_is_empty():
    deque = Deque[int]()
    assert deque.is_empty() == True

    deque.push_back(1)
    assert deque.is_empty() == False

    deque.pop_back()
    assert deque.is_empty() == True
