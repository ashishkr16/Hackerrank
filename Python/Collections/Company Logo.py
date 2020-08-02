import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = sorted(input().strip())
    S_counter = collections.Counter(s).most_common()

    S_counter = sorted(S_counter, key=lambda x: (x[1] * -1, x[0]))
    for i in range(0,3):
        print(S_counter[i][0], S_counter[i][1])