# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math


def calc_impossible(posantX, d, h, dis):
    r = (d / 2)
    height = math.sqrt((r ** 2 - (dis - posantX - r) ** 2)) + h
    return height < h


# Calculating the arc radius

def radius(values):
    dis = []  # Distance
    disAnt = []  # Distance
    alt = []  # Height
    antdistancia = -50

    for pos in values:

        x, y = medides(pos)
        alt.append(y)

        if antdistancia != -50:
            dis.append(x - antdistancia)
            disAnt.append(x)
        antdistancia = x

    return dis, alt, disAnt


def medides(values):
    x = values[0]
    y = values[1]

    return x, y


# This method calculates the total costs.

def costos(n, alpha, beta, h, dis, alt, disAnt):
    costosAltura = 0
    costosDistancia = 0
    esposible = True
    for i in range(0, n):
        n = n + 1

        esposible = calc_impossible(disAnt[i], dis[i], h, )
        costosAltura += (h - alt[i])
        if i < n - 1:
            costosDistancia += (dis[i] ** 2)

    resultado = (alpha * costosAltura) + (beta * costosDistancia)
    return resultado
