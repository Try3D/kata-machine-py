def BinarySearch(arr: list[int], target: int) -> int:
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            start = middle + 1
        if arr[middle] > target:
            end = middle - 0

    return -1
