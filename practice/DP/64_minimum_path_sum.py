import sys
from typing import List
from math import inf


class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [[0, 0, 0]] * (self.maxsize + 1)
        self.Heap[0][0] = -1 * sys.maxsize
        self.FRONT = 1

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize:
            return

        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        while self.Heap[current][0] < self.Heap[self.parent(current)][0]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # Function to print the contents of the heap
    def Print(self):
        print("Heap:", self.Heap)

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos][0] > self.Heap[self.leftChild(pos)][0] or
                    self.Heap[pos][0] > self.Heap[self.rightChild(pos)][0]):

                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)][0] < self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to remove and return the minimum
    # element from the heap
    def remove(self):

        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped


class Solution:
    def minPathSum(self, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        dp = [[inf for _ in range(m)] for _ in range(n)]
        heap = MinHeap(n * m)
        dp[0][0] = grid[0][0]

        def expand(i, j):
            nonlocal n, m
            # Down
            if i != n - 1:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + grid[i + 1][j])

            # Right
            if j != m - 1:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + grid[i][j + 1])

        i = 0
        j = 0
        heap.insert([dp[0][0], i, j])
        while True:
            _, i, j = heap.remove()
            if i == n - 1 and j == m - 1:
                break
            expand(i, j)
            if i != n - 1:
                heap.insert([dp[i + 1][j], i + 1, j])

            if j != m - 1:
                heap.insert([dp[i][j + 1], i, j + 1])

        return dp[n - 1][m - 1]


sol = Solution()
print(sol.minPathSum(
    [
        [1, 4, 8, 6, 2, 2, 1, 7],
        [4, 7, 3, 1, 4, 5, 5, 1],
        [8, 8, 2, 1, 1, 8, 0, 1],
        [8, 9, 2, 9, 8, 0, 8, 9],
        [5, 7, 5, 7, 1, 8, 5, 5],
        [7, 0, 9, 4, 5, 6, 5, 6],
        [4, 9, 9, 7, 9, 1, 9, 0]]))
