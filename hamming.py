# Module hamming.py
import numpy as np

def hammingWeight(x):
    count = 0
    for i in range(8):
        shifted = np.right_shift(x, i)
        if np.bitwise_and(shifted, 1 == 1):
            count = count + 1

    return count
