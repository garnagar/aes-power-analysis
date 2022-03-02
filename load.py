import numpy as np

def loadFloats(path):
    with open(path, "r") as f:
        return np.loadtxt(f, delimiter=",")

def loadInts(path):
    with open(path, "r") as f:
        return np.loadtxt(f, delimiter=",", dtype="int")