from time import *
import random
from matplotlib import pyplot as plt

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