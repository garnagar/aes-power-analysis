import numpy as np

def calcCorrelationMatrix(T, H):
    # Prepare variables
    samplesCount = T.shape[0]
    keyCount = H.shape[0]
    assert T.shape[1] == H.shape[1]  # Check if the number of plaintexts is the same
    C = np.zeros([samplesCount, keyCount])

    # Calculate correlation
    for i in range(keyCount):
        for j in range(samplesCount):
            C[i, j] = np.corrcoef(H[:, i].T, T[:, j].T)

    return C