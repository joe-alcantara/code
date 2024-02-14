'''
Demonstrate o(n)
Demonstrate o(1)
Demonstrate o(n^2)


'''

from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib as plt
import random

'''
findSum is a function that takes a list of numbers
It returns the sum of the numbers within the list
'''


def findSum(listNum):
    total = 0
    for i in listNum:
        total = total + i
    return total


def process(x):
    # record current timestamp
    start = datetime.now()

    findSum(x)

    # record loop end timestamp
    end = datetime.now()

    # find difference loop start and end time and display
    td = (end - start).total_seconds() * 10 ** 3
    return td


def generate(x):
    randomlist = []
    for i in range(x):
        n = random.randint(1, 30)
        randomlist.append(n)
    return randomlist


def repeat(x):
    times = []
    for i in range(x):
        testlist = generate(2048)
        time = process(testlist)
        times.append(time)
    return times


# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)


times = repeat(200)
mean = Average(times)
print(mean)

# testlist = generate(5)
# time = process(testlist)

#Joe adding a comment at 10.11am
#Joe adding a comment at 11:18am