#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    neutral = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            positive += 1
        elif arr[i] == 0:
            neutral += 1
        else:
            negative += 1
    print(positive/len(arr))
    print(negative/len(arr))
    print(neutral/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
