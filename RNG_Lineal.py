import numpy as np

def RNG_Lineal(a,c,m,X_0):
    X = np.zeros(m)
    X[0] = X_0
    for i in range(0,m-1):
        X[i+1] = np.mod((a*X[i]) + c, m)
    return X

modulo = 10
sequence = RNG_Lineal(2,3,modulo,0)
sequence_norm = sequence/modulo
print("X_n", sequence)
print("X_n/m", sequence_norm)