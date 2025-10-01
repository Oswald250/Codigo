import numpy as np

z = np.array([1.0, -4, -2, 0, 0, 0, 0])

Eq = np.array([

    [0.0, 1, 2, 1, 0, 0, 0],
    [0,   2, 1, 0, 1, 0, 0],
    [0,  -1, 1, 0, 0, 1, 0],
    [0,   0, 1, 0, 0, 0, 1]
])

b = np.array([6, 8, 1,2])  

def armarTablero(f,A,B): return np.hstack((np.vstack((f,A)), np.insert(B,0,0)[:,None]))

def maximizar(t):

    while np.any(t[0, :-1] < 0):
        cp = np.argmin(t[0, :-1])
        r = t[1:, -1] / t[1:, cp]
        r[r <= 0] = np.inf
        fp = np.argmin(r) + 1
        t[fp] /= t[fp, cp]
        for i in range(len(t)):
            if i != fp:
                t[i] -= t [i, cp] * t[fp]

    return t

tablero = armarTablero(z, Eq, b)
res = maximizar(tablero)
print(res)
print("Z =", res[0, -1])