from exercises.binary_search import BinarySearch


def test_binary_search_found():
    arr = [1, 2, 3, 4, 5]
    target = 3
    assert BinarySearch(arr, target) == 2


def test_binary_search_not_found():
    arr = [1, 2, 3, 4, 5]
    target = 6
    assert BinarySearch(arr, target) == -1


def test_binary_search_empty_list():
    arr = []
    target = 5
    assert BinarySearch(arr, target) == -1


def test_binary_search_duplicate_elements():
    arr = [1, 2, 3, 3, 4, 5]
    target = 3
    assert BinarySearch(arr, target) == 2


def test_binary_search_first_element():
    arr = [1, 2, 3, 4, 5]
    target = 1
    assert BinarySearch(arr, target) == 0


def test_binary_search_last_element():
    arr = [1, 2, 3, 4, 5]
    target = 5
    assert BinarySearch(arr, target) == 4
