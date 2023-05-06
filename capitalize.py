import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        res=s.replace(i, i.capitalize())
    return res
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter name:")

    result = solve(s)

    print(str(result) + '\n')

    # fptr.close()
