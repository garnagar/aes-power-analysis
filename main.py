"""
Project: AES Differential Power Analysis
Authors: Lukas Kyzlik, William Wulff
Date: 9/3/2022

Description:
The script implements attack on AES using differential power analysis. Key byte can be discovered correlating power
consumption traces (input file T1.dat) with Hamming weights of simulated traces, both for vector of plaintexts
(input1.dat).
"""

import numpy as np
import matplotlib.pyplot as plt
from sbox import SBOX


def loadInts(path):
    """
    Loads integer data from a file into 1D or 2D numpy array.
    """
    with open(path, "r") as f:
        return np.loadtxt(f, delimiter=",", dtype="int")


def loadFloats(path):
    """
    Loads floating point data from a file into 1D or 2D numpy array.
    """
    with open(path, "r") as f:
        return np.loadtxt(f, delimiter=",")


def hammingWeight(x):
    """
    Calculates Hamming weight (hw) of x. Hamming weight is a number of 1s in binary representation.
    """
    count = 0
    for i in range(8):
        shifted = np.right_shift(x, i)
        if np.bitwise_and(shifted, 1 == 1):
            count = count + 1

    return count


def aesRound(keyByte, plaintextByte):
    """
    Calculates value of plaintext byte after passing first round of AES. Plaintext byte is XORed with key byte and
    replaced by S-box lookup.
    """
    return SBOX[np.bitwise_xor(keyByte, plaintextByte)]


def calcHammingMatrix(vector):
    """
    Returns matrix H. H(i,j) is Hamming weight of byte after first round of AES where i = 0..N-1 is plaintext vector
    index and j = 0..(2^8)-1 is key byte value (all possible key bytes are calculated). I.e., j-th column represents
    values that should correlate with power consumption if j is correct key byte.
    """
    H = []
    for x in range(len(vector)):
        temp = [hammingWeight(aesRound(k, vector[x])) for k in range(256)]
        H.append(temp)

    return np.array(H)

def calcCorrelationMatrix(T, H):
    """
    Returns matrix C. C(i,j) is correlation of power consumption in time i and Hamming weights for key byte j. T is
    matrix where each row contains power consumption for one plaintext byte. H is matrix obtained from calcHammingMatrix
    function.
    """
    # Prepare variables
    samplesCount = T.shape[1]
    keyCount = H.shape[1]
    C = np.zeros([keyCount, samplesCount])

    # Calculate correlation
    for i in range(keyCount):
        for j in range(samplesCount):
            C[i, j] = np.corrcoef(H[:, i].T, T[:, j].T)[0, 1]

    return C


def getKeyByte(C):
    """
    Returns key byte and its absolute correlation. The correlation is the highest absolute value in C matrix and the key
    is index of its column.
    """
    maxVal = np.amax(np.abs(C))
    keyByte = np.where(np.abs(C) == maxVal)[0][0]  # key byte = index of a column with max absolute value
    return keyByte, maxVal

def debugPlotAllCorrelations(C, k):
    for i in range(C.shape[1]):
        plt.plot(range(C.shape[1]), np.abs(C[i, :]), "#c4c4c4")
    plt.plot(range(C.shape[1]), np.abs(C[k, :]), "r", label="key byte " + hex(k))
    plt.ylabel("Absolute correlation [-]")
    plt.xlabel("Sample")
    plt.legend()
    plt.title("Correlations for all key bytes (best correlation in red)")
    plt.show()

def main():
    T = loadFloats("data/T1.dat")
    H = calcHammingMatrix(loadInts("data/inputs1.dat"))
    C = calcCorrelationMatrix(T, H)
    k, corr = getKeyByte(C)
    print("Key byte is {} == {} with max absolute value of correlation {}".format(hex(k), k, np.round(corr, 4)))
    debugPlotAllCorrelations(C, k)

if __name__ == '__main__':
    main()

