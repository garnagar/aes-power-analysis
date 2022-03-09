import numpy as np

def calcCorrelationMatrix(T, H):
    # Prepare variables
    samplesCount = T.shape[1]
    keyCount = H.shape[1]
    assert T.shape[0] == H.shape[0]  # Check if the number of plaintexts is the same
    C = np.zeros([keyCount, samplesCount])

    # Calculate correlation
    for i in range(keyCount):
        for j in range(samplesCount):
            C[i, j] = np.corrcoef(H[:, i].T, T[:, j].T)[0, 1]

    return C