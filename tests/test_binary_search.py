from exercises.binary_search import BinarySearch


def test_binary_search_found():
    assert BinarySearch([1, 2, 3, 4, 5], 3) == 2


def test_binary_search_not_found():
    assert BinarySearch([1, 2, 3, 4, 5], 6) == -1


def test_binary_search_empty_list():
    assert BinarySearch([], 5) == -1


def test_binary_search_duplicate_elements():
    assert BinarySearch([1, 2, 3, 3, 4, 5], 3) == 2


def test_binary_search_first_element():
    assert BinarySearch([1, 2, 3, 4, 5], 1) == 0


def test_binary_search_last_element():
    assert BinarySearch([1, 2, 3, 4, 5], 5) == 4
