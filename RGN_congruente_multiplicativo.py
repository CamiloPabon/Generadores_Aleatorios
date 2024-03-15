import numpy as np

def RNG_multiplicativo(a,m,X_0):
    X = np.zeros(m)
    X[0] = X_0
    for i in range(0,m-1):
        X[i+1] = np.mod((a*X[i]), m)
    return X

modulo = 16
sequence = RNG_multiplicativo(4,modulo,8)
sequence_norm = sequence/modulo
print("X_n", sequence)
print("X_n/m", sequence_norm)