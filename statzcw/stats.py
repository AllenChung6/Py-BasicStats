from typing import List
from math import floor, ceil, sqrt
import csv


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


# Standard deviation divided by the square root of the number of values.
def zstderr(list: List[float]) -> float:
    standard_error = zstddev(list) / sqrt(zcount(list))
    return standard_error


def zcovar(listx: List[float], listy: List[float]) -> float:
    sum = 0
    if zcount(listx) == zcount(listy):
        for i in range(0, zcount(listx)):
            sum += ((listx[i] - zmean(listx)) * (listy[i] - zmean(listy)))
        covariance = sum / (zcount(listx) - 1)
        return covariance


# correlation(l1, l2) = covariance(l1, l2) / (stddev(l1) * stddev(l2))
def zcorr(listx: List[float], listy: List[float]) -> float:
    correlation = zcovar(listx, listy) / (zstddev(listx) * zstddev(listy))
    return correlation


def read_data_sets(file_path):
    header = []
    try:
        listx = []
        listy = []
        list_xy = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            listx = []
            listy = []
            for row in reader:
                listx.append(row[0])
                listy.append(row[1])
            list_xy.append(listx)
            list_xy.append(listy)
        return list_xy
    except TypeError:
        print('')


data0 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataZero.csv'
data1 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataOne.csv'
data2 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataTwo.csv'
data3 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataThree.csv'
dataset0 = read_data_sets(data0)
dataset1 = read_data_sets(data1)
dataset2 = read_data_sets(data2)
dataset3 = read_data_sets(data3)

# Dataset 0 stats
print(f'Data set 0: \nCount of x is {zcount(dataset0[0])}')
