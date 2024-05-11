from exercises.linear_search import LinearSearch


def test_linear_search_found():
    arr = [1, 2, 3, 4, 5]
    target = 3
    assert LinearSearch(arr, target) == 2


def test_linear_search_not_found():
    arr = [1, 2, 3, 4, 5]
    target = 6
    assert LinearSearch(arr, target) == -1


def test_linear_search_empty_list():
    arr = []
    target = 5
    assert LinearSearch(arr, target) == -1


def test_linear_search_duplicate_elements():
    arr = [1, 2, 3, 3, 4, 5]
    target = 3
    assert LinearSearch(arr, target) == 2


def test_linear_search_first_element():
    arr = [1, 2, 3, 4, 5]
    target = 1
    assert LinearSearch(arr, target) == 0


def test_linear_search_last_element():
    arr = [1, 2, 3, 4, 5]
    target = 5
    assert LinearSearch(arr, target) == 4
