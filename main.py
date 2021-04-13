# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import read_file
import calculs

if __name__ == "__main__":
    values, n, h, alpha, beta = read_file.read_file("testing/test5-1.in", data_separation=" ")
    # values = List of tuples (x, y), n = number of columns, h = required height, alpha & beta = cost factors
    rad, dis, alt = calculs.radius(values)  # radius, distance, height

    print("\n Values")
    print("------------------ ")
    print(values)
    print("\n distancia entre cada punto")
    print("------------------ ")
    print(dis)
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
    print(calculs.costos(n, alpha, beta, h, dis, alt))
