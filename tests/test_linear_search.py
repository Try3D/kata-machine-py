from exercises.linear_search import LinearSearch


def test_linear_search_found():
    assert LinearSearch([1, 2, 3, 4, 5], 3) == 2


def test_linear_search_not_found():
    assert LinearSearch([1, 2, 3, 4, 5], 6) == -1


def test_linear_search_empty_list():
    assert LinearSearch([], 5) == -1


def test_linear_search_duplicate_elements():
    assert LinearSearch([1, 2, 3, 3, 4, 5], 3) == 2


def test_linear_search_first_element():
    assert LinearSearch([1, 2, 3, 4, 5], 1) == 0


def test_linear_search_last_element():
    assert LinearSearch([1, 2, 3, 4, 5], 5) == 4
