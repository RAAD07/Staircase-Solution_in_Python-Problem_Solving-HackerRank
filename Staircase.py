#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    row=1
    while row<=n:
        space=n
        while space>row:
            print(" ",end="")
            space=space-1
        hash=1
        while hash<=row:
            print("#",end="")
            hash=hash+1
        print()
        row=row+1



if __name__ == '__main__':
    n = int(input())

    staircase(n)
