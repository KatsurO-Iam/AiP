sp = [1,3,4,2,5,7,3,5,8,2,9,3,4,6,7]
def bubble_sort(s):
    s = s[:]
    for i in range(len(s)-1):
        for j in range(len(s) - 1 - i):
            if s[j] > s[j + 1]:
                s[j], s[j + 1] = s[j + 1], s[j]
    return s
from time import *

start = perf_counter()
sleep(1)
end = perf_counter()
print(end - start)

import random

print([random.randint(1,100) for i in range(10)])

from matplotlib import pyplot as plt

# plt.plot([1,2,3,4], [1,4,9,16])
# plt.plot([1,2,3,4], [-1,-4,-9,-16])
# plt.show()

def linear_search(arr, t):
    for i, x in enumerate(arr):
        if x == t:
            return i
    return -1

def binary_search(arr, t):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

line_time = []
binary_time = []

for i in range(10_000, 1_000_000, 10_000):
    a = [j for j in range(i)]
    start_linear = perf_counter()
    linear_search(a, a[-1])
    end_linear = perf_counter()
    start_bin = perf_counter()
    binary_search(a, a[-1])
    end_bin = perf_counter()
    line_time.append(end_linear - start_linear)
    binary_time.append(end_bin - start_bin)

plt.plot(range(10_000, 1_000_000, 10_000), line_time)
plt.plot(range(10_000, 1_000_000, 10_000), binary_time)
plt.show()