from collections import deque
from math import ceil, comb
mundo = [1, 2, 3, 4]
hola = deque([(0, elem) for elem in mundo])
hola.append((5, 1))
print(hola)
print(hola.popleft()[0])
print(hola)
hola.pop

a = "0"
b = "1"
print(((a == "1") and not (b == "1")) or (not (a == "1") and (b == "1")))
print(ord("1") + ord("0"))
print(min(1, -float('Inf')))
tst = [1, 2, 3, 4, 5]
k = 4
print(tst[:k])
heap = tst[:k]
print(heap)



def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


swap(heap, 0, 2)
print(heap)
print(ceil((6 + 7) / 2))
print(comb(4, 4), comb(5, 4), comb(6, 4), comb(7, 4))

rwk = set()
uwa = [1, 2, 3]
rwk = rwk.union(uwa)
print(rwk, "hola", 1 & 0)
olia = 1
olia &= 1
print(olia)
olia &= 0
print(olia)
print(len([1,8,6,2,5,4,8,3,7]))