from typing import TypeVar, Union


T = TypeVar("T")


class Heap:
    def __init__(self):
        self.heap: list[int] = []

    def insert(self, value: int):
        self.heap.append(value)

        idx = len(self.heap) - 1

        while idx > 0:
            p_idx = (idx - 1) // 2

            if self.heap[p_idx] < self.heap[idx]:
                self.heap[p_idx], self.heap[idx] = self.heap[idx], self.heap[p_idx]
            else:
                break

    def remove(self) -> Union[int, None]:
        if not self.heap:
            return None

        max_value = self.heap[0]

        self.heap[0] = self.heap.pop()

        index = 0
        while True:
            l_idx = 2 * index + 1
            r_idx = 2 * index + 2

            if l_idx >= len(self.heap):
                break

            max_idx = l_idx

            if r_idx < len(self.heap) and self.heap[r_idx] > self.heap[l_idx]:
                max_idx = r_idx
            if self.heap[index] < self.heap[max_idx]:
                self.heap[index], self.heap[max_idx] = self.heap[max_idx], self.heap[index]
                index = max_idx
            else:
                break
        return max_value

    def array(self) -> list[int]:
        return self.heap
