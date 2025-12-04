import numpy as np

n = int(input("Numero de variables; "))
m = int(input("Numero de restricciones; "))

c = np.array([float(input(f"c{i+1}: ")) for i in range(n)])
a = []
b = []
for i in range(m):
    fila = [float(input(f"a{i+1},{j+1}:")) for j in range(n)]
    a.append(fila)
    b.append(float(input(f"b{i+1}: ")))

a = np.array(a)
b = np.array(b)

tableau = np.zeros((m + 1, n + m + 1))
tableau[:m, :n] = a
tableau[:m, n:n + m] = np.eye(m)
tableau[:m, -1] = b
tableau[-1, :n] = -c
basis = list(range(n,n + m))

while True:

    if all(tableau[-1, :-1] >= 0):
        break
    col = np.argmin(tableau[-1, :-1])
    if all(tableau[:m, col] <= 0):
     print("Problema ilimitado")
     exit()
    
    raritos = [tableau[i, -1] / tableau[i, col] 
            if tableau[i, col] > 0 else np.inf for i in range(m)]
    row = np.argmin(raritos)
    pivot = tableau[row, col]
    tableau[row, :] /= pivot

    for i in range(m + 1):
       if i != row:
            factor = tableau[i,col]
            tableau[i, :] -= factor * tableau[row, :]

            basis[row] = col

    x = np.zeros(n + m)
    x[basis] = tableau[:m, -1]


    print("\n === Resultado final ===")        
    for i in range(n + m):
     print(f"x{i+1} = {x[i]}")
    print("Valor Maximo:", tableau[-1, -1])


