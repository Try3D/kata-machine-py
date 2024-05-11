from exercises.merge_sort import MergeSort


def test_merge_sort_empty_array():
    arr = []
    assert MergeSort(arr) == []


def test_merge_sort_single_element():
    arr = [5]
    assert MergeSort(arr) == [5]


def test_merge_sort_already_sorted():
    arr = [1, 2, 3, 4, 5]
    assert MergeSort(arr) == [1, 2, 3, 4, 5]


def test_merge_sort_reverse_sorted():
    arr = [5, 4, 3, 2, 1]
    assert MergeSort(arr) == [1, 2, 3, 4, 5]


def test_merge_sort_random_order():
    arr = [3, 5, 1, 2, 4]
    assert MergeSort(arr) == [1, 2, 3, 4, 5]


def test_merge_sort_duplicates():
    arr = [4, 2, 3, 2, 1]
    assert MergeSort(arr) == [1, 2, 2, 3, 4]


def test_merge_sort_negative_numbers():
    arr = [4, -2, 3, -5, 1]
    assert MergeSort(arr) == [-5, -2, 1, 3, 4]


def test_merge_sort_mixed_numbers():
    arr = [-2, 3, -5, 1, 0, -4, 6]
    assert MergeSort(arr) == [-5, -4, -2, 0, 1, 3, 6]
