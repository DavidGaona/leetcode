from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    n = len(nums) - k + 1
    max_at = [0] * n
    heap = nums[:k]
    # key: Pos in nums -> val: pos in heap
    pos = {}
    pos_inv = {}
    for i in range(k):
        pos[i] = i
        pos_inv[i] = i

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heapify(arr, n, i):
        original = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[i]:
            i = left

        if right < n and arr[right] > arr[i]:
            i = right

        if i != original:
            swap(arr, original, i)
            pos[i], pos[original] = pos[original], pos[i]
            heapify(arr, n, i)

    def heapify_up(arr, n, i):
        parent = abs(i - 1) // 2

        if arr[i] > arr[parent]:
            swap(arr, parent, i)
            pos[i], pos[parent] = pos[parent], pos[i]
            heapify(arr, n, parent)

    def build_max_heap(arr):
        for i in range((k // 2) - 1, -1, -1):
            heapify(arr, k, i)

    print(heap, pos)
    build_max_heap(heap)
    print(heap, pos, n)
    max_at[0] = heap[0]
    for i in range(1, n):
        heap[pos[i - 1]] = nums[i + k - 1]
        pos[i + k - 1] = pos[i - 1]
        del pos[i - 1]
        heapify(heap, k, pos[i + k - 1])
        #heapify_up(heap, k, pos[i + k - 1])
        max_at[i] = heap[0]
        print(i, i + k - 1)
    print(max_at)
    return [3, 3, 5, 5, 6, 7]


maxSlidingWindow([1, 3, -1, 8, 5, 3, 6, 7], 3)
