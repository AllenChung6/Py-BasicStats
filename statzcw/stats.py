from typing import List
from math import floor, ceil, sqrt


def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    total = sum(list)
    mean = total / zcount(list)
    return mean


def zmode(list: List[float]) -> float:
    return max(set(list), key=list.count)


# Take the middle number. If it is an even list, sort the list and take the mean of the middle two numbers.
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


# Take the mean. Take each value, subtract the mean, square the difference. Add all squared differences and divide by number of values.
def zvariance(list: List[float]) -> float:
    # Calculate First Part
    mean = zmean(list)
    # Calculate Second Part
    new_list = [(x - mean) ** 2 for x in list if True]
    # Calculate Thid Part
    variance = zmean(new_list)
    return variance


# Square Root the variance
def zstddev(list: List[float]) -> float:
    variance = zvariance(list)
    standard_deviation = sqrt(variance)
    return standard_deviation


def zstderr(list: List[float]) -> float:


list = [7, 10, 14, 12, 14]
print(zstddev(list))
