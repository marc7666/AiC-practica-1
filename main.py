# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import read_file
import calculs

if __name__ == "__main__":

    values, n, h, alpha, beta = read_file.read_file("testing/test5-2.in", data_separation=" ")
    dis, alt, disAnt = calculs.obtainValues(values)

    print("\n Values")
    print("------------------ ")
    print(values)
    print("\n distancia entre cada punto")
    print("------------------ ")
    print(dis)
    print(alt)
    print("\n columnas/puntos")
    print("------------------ ")
    print(n)
    print("\n Altura requerida")
    print("------------------ ")
    print(h)
    print("\n Alpha")
    print("------------------ ")
    print(alpha)
    print("\n Beta")
    print("------------------ ")
    print(beta)
    print("\n Total sum")
    print("------------------ ")
    resultado=calculs.costsAque(n, alpha, beta, h, values)
    print(resultado)
