from exercises.stack import Stack


def test_stack_push():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2


def test_stack_pop():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2


def test_stack_peek():
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2


def test_stack_is_empty():
    stack = Stack[int]()
    assert stack.is_empty() == True

    stack.push(1)
    assert stack.is_empty() == False

    stack.pop()
    assert stack.is_empty() == True
