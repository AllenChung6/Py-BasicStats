from typing import List
from math import floor, ceil


def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    total = sum(list)
    mean = total / zcount(list)
    return mean


def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)


def zmedian(list: List[float]) -> float:
    if zcount(list) % 2 == 0:
        # Takes the middle index
        median = zcount(list) / 2
        # Rounds the middle index up
        median = ceil(median)
        # Creates another index before the middle index
        median2 = median - 1
        sorted_list = sorted(list)
        mean = (sorted_list[median] + sorted_list[median2]) / 2
        return mean
    else:
        median = zcount(list) / 2
        median = floor(median)
        return list[median]


list = [267, 19, 43, 2000, ]
print(zmedian(list))
