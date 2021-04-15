# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math

def calc_impossible(posX, d, alt):
    r = (d / 2)
    height = math.sqrt((r ** 2 - (posX-r) ** 2))+alt
    return height < alt


# Calculating the arc radius

def radius(values):
    rad = []  # Radius
    dis = []  # Distance
    alt = []  # Height
    antdistancia = -50

    for pos in values:

        int1, int2 = medides(pos)
        rad.append(math.sqrt(int1 ** 2 + int2 ** 2))  # radius formula
        alt.append(int2)

        if antdistancia != -50:
            dis.append(int1 - antdistancia)

        antdistancia = int1

    return rad, dis, alt


def medides(values):
    int1 = values[0]
    int2 = values[1]

    return int1, int2


# This method calculates the total costs.

def costos(n, alpha, beta, h, dis, alt):
    costosAltura = 0
    costosDistancia = 0

    for i in range(0, n):

        costosAltura += (h - alt[i])
        if i < n - 1:
            costosDistancia += (dis[i] ** 2)

    resultado = (alpha * costosAltura) + (beta * costosDistancia)
    return resultado
