from exercises.insertion_sort import InsertionSort


def test_insertion_sort_empty_array():
    arr = []
    assert InsertionSort(arr) == []


def test_insertion_sort_single_element():
    arr = [5]
    assert InsertionSort(arr) == [5]


def test_insertion_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert InsertionSort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert InsertionSort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_random_order():
    arr = [3, 5, 1, 2, 4]
    assert InsertionSort(arr) == [1, 2, 3, 4, 5]


def test_insertion_sort_duplicates():
    arr = [4, 2, 3, 2, 1]
    assert InsertionSort(arr) == [1, 2, 2, 3, 4]


def test_insertion_sort_negative_numbers():
    arr = [4, -2, 3, -5, 1]
    assert InsertionSort(arr) == [-5, -2, 1, 3, 4]


def test_insertion_sort_mixed_numbers():
    arr = [-2, 3, -5, 1, 0, -4, 6]
    assert InsertionSort(arr) == [-5, -4, -2, 0, 1, 3, 6]
