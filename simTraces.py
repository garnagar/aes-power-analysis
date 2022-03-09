import numpy as np
import sbox as box
import load as ld
import hamming as hm

def aesRound(keyByte, plaintextByte):
    return box.SBOX[ np.bitwise_xor(keyByte, plaintextByte) ] 

# Returns h(i,j) where i = 0..N-1 and j = 0..(2^8)-1
# i is plaintext index and j is keybyte index (the index is also the key value)
def generateSimTrace(vectorPath):
    vector = ld.loadInts(vectorPath)
    H = []
    temp = []
    for x in range(len(vector)):
        temp = [ hm.hammingWeight( aesRound(k, vector[x]) ) for k in range(256) ]
        H.append(temp)
        
    # Transpose the matrix to get the right format
    # H(j,i) -> H(i,j)
    return np.array(H) #list(zip(*H))
