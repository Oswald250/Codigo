import numpy as np

z = np.array([1.0, -4, -2, 0, 0, 0, 0])

Eq = np.array([

    [0.0, 1, 2, 1, 0, 0, 0],
    [0,   2, 1, 0, 1, 0, 0],
    [0,  -1, 1, 0, 0, 1, 0],
    [0,   0, 1, 0, 0, 0, 1]
])

b = np.array([6, 9, 1,2])  

def armarTablero(f,A,B): return np.hstack((np.vstack((f,A)), np.insert(B,0,0)[:,None]))

def maximizar(t):

    while np.any(t[0, :-1] < 0):
        while np.any(t[0, :-1] <0 ):
            col = np.argmin(t[0, :-1])
            razones = t[1:, -1]/ t[1:, col]
            razones[razones <= 0] = np.inf
            fila = np.argmin(razones) + 1
            
            t[fila] = t[fila] / t [fila, col] *  t[fila]

            for i in range(len(t)):
                if i != fila:
    
                 t[i] = t[i] - t[i,col] * t[fila]

    return t

tablero = armarTablero(z, Eq, b)
res = maximizar(tablero)
print(res)
print("Z =", res[0, -1])