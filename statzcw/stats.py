from typing import List
from math import floor, ceil, sqrt
import csv


def zcount(list: List[float]) -> float:
    return len(list)


def zmean(list: List[float]) -> float:
    mean = (sum(list)) / zcount(list)
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


def read_data_sets_x(file_path):
    header = []
    try:
        listx = []
        listy = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            listx = []
            listy = []
            for row in reader:
                listx.append(row[0])
    except TypeError:
        print('')
    return [float(x) for x in listx]


def read_data_sets_y(file_path):
    header = []
    try:
        listy = []
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            listy = []
            for row in reader:
                listy.append(row[1])
    except TypeError:
        print('')
    return [float(x) for x in listy]


# .csv file paths
data0 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataZero.csv'
data1 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataOne.csv'
data2 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataTwo.csv'
data3 = '/Users/allenc/PyCharmProjects/Py-BasicStats/dataThree.csv'

dataset0_x = read_data_sets_x(data0)
dataset1_x = read_data_sets_x(data1)
dataset2_x = read_data_sets_x(data2)
dataset3_x = read_data_sets_x(data3)

dataset0_y = read_data_sets_y(data0)
dataset1_y = read_data_sets_y(data1)
dataset2_y = read_data_sets_y(data2)
dataset3_y = read_data_sets_y(data3)

# Dataset 0 stats
print(
    f'Data set 0: \nCount of x: {zcount(dataset0_x)} \nCount of y: {zcount(dataset0_y)} \nMean of x: {zmean(dataset0_x)}\n\
Variance of x: {zvariance(dataset0_x)}\nMean of y: {zmean(dataset0_y)}\nVariance of y: {zvariance(dataset0_y)}\n\
Correlation of x, y: {zcorr(dataset0_x, dataset0_y)}\nMedian of x: {zmedian(dataset0_x)}\nMedian of Y: {zmedian(dataset0_y)}\n\
Mode of x: {zmode(dataset0_x)}\nMode of y: {zmode(dataset0_y)}\nStd deviation of x: {zstddev(dataset0_x)}\n\
Std deviation of y: {zstddev(dataset0_y)}\nStd Error of x: {zstderr(dataset0_x)}\nStd Error of y: {zstderr(dataset0_y)}')

# Dataset 1 stats
print(
    f'\nData set 1: \nCount of x: {zcount(dataset1_x)} \nCount of y: {zcount(dataset1_y)} \nMean of x: {zmean(dataset1_x)}\n\
Variance of x: {zvariance(dataset1_x)}\nMean of y: {zmean(dataset1_y)}\nVariance of y: {zvariance(dataset1_y)}\n\
Correlation of x, y: {zcorr(dataset1_x, dataset1_y)}\nMedian of x: {zmedian(dataset1_x)}\nMedian of Y: {zmedian(dataset1_y)}\n\
Mode of x: {zmode(dataset1_x)}\nMode of y: {zmode(dataset1_y)}\nStd deviation of x: {zstddev(dataset1_x)}\n\
Std deviation of y: {zstddev(dataset1_y)}\nStd Error of x: {zstderr(dataset1_x)}\nStd Error of y: {zstderr(dataset1_y)}')

# Dataset 2 stats
print(
    f'\nData set 2: \nCount of x: {zcount(dataset2_x)} \nCount of y: {zcount(dataset2_y)} \nMean of x: {zmean(dataset2_x)}\n\
Variance of x: {zvariance(dataset2_x)}\nMean of y: {zmean(dataset2_y)}\nVariance of y: {zvariance(dataset2_y)}\n\
Correlation of x, y: {zcorr(dataset2_x, dataset2_y)}\nMedian of x: {zmedian(dataset2_x)}\nMedian of Y: {zmedian(dataset2_y)}\n\
Mode of x: {zmode(dataset2_x)}\nMode of y: {zmode(dataset2_y)}\nStd deviation of x: {zstddev(dataset2_x)}\n\
Std deviation of y: {zstddev(dataset2_y)}\nStd Error of x: {zstderr(dataset2_x)}\nStd Error of y: {zstderr(dataset2_y)}')

# Dataset 3 stats
print(
    f'\nData set 3: \nCount of x: {zcount(dataset3_x)} \nCount of y: {zcount(dataset3_y)} \nMean of x: {zmean(dataset3_x)}\n\
Variance of x: {zvariance(dataset3_x)}\nMean of y: {zmean(dataset3_y)}\nVariance of y: {zvariance(dataset3_y)}\n\
Correlation of x, y: {zcorr(dataset3_x, dataset2_y)}\nMedian of x: {zmedian(dataset3_x)}\nMedian of Y: {zmedian(dataset3_y)}\n\
Mode of x: {zmode(dataset3_x)}\nMode of y: {zmode(dataset3_y)}\nStd deviation of x: {zstddev(dataset3_x)}\n\
Std deviation of y: {zstddev(dataset3_y)}\nStd Error of x: {zstderr(dataset3_x)}\nStd Error of y: {zstderr(dataset3_y)}')
