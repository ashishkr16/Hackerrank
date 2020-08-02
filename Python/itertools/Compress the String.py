#!/usr/bin/env python

from itertools import *

for i, j in groupby(map(int, list(input()))):
    print(tuple([len(list(j)), i]), end=" ")
