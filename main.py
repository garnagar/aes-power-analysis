from load import loadFloats, loadInts
from simTraces import generateSimTrace
from corr import calcCorrelationMatrix

def main():
    T = loadFloats("data/T1.dat")
    H = generateSimTrace("data/inputs1.dat")
    C = calcCorrelationMatrix(T, H)
    print(C)

if __name__ == '__main__':
    main()

