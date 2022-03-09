from load import loadFloats, loadInts
from simTraces import generateSimTrace
from corr import calcCorrelationMatrix
import matplotlib.pyplot as plt

def main():
    T = loadFloats("data/T1.dat")
    H = generateSimTrace("data/inputs1.dat")
    C = calcCorrelationMatrix(T, H)
    print(C)

    # Graphic test to show correlation for
    # test dataset (correct keybyte = 203 DEC)
    T = loadFloats("data/T_test.dat")
    H = generateSimTrace("data/inputs_test.dat")
    C = calcCorrelationMatrix(T, H)
    
    plt.plot(C[0,:], label='Keybyte 0')
    plt.plot(C[50,:], label='Keybyte 50')
    plt.plot(C[203,:], label='Keybyte 203')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()

