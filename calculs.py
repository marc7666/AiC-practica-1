# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math


# Calculating the arc radius

def radius(values):
    rad = []  # Radius
    dis = []  # Distance
    alt = []  # Height
    antdistancia = 0  # Previous distance

    for pos in values:

        int1, int2 = medides(pos)  # int1 = x && int2 = y
        rad.append(math.sqrt(int1 ** 2 + int2 ** 2))  # radius formula
        alt.append(int2)

        if antdistancia != 0:
            dis.append(int1 - antdistancia)

        antdistancia = int1

    return rad, dis, alt


# This method returns the coordinates of a tuple tuple (x, y)

def medides(values):
    int1 = values[0]
    int2 = values[1]

    return int1, int2


# This method calculates the total costs.

def costos(n, alpha, beta, h, dis, alt):
    costosAltura = 0
    costosDistancia = 0

    for i in range(0, n):  # 0 to n => Chek all the key points

        costosAltura += alpha * (h - alt[i])
        if i < n - 1:
            costosDistancia += (beta * (dis[i] ** 2))

    resultado = costosAltura + costosDistancia

    return resultado
