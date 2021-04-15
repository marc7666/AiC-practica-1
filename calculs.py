# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math


# Calculating posibility create pont
def calc_impossiblepont(posantX, d, h, disX):
    r = (d / 2)
    height = math.sqrt((r ** 2 - (disX - posantX - r) ** 2)) + h
    return height < h


# Calculating posibility create aqueduct
def calc_impossible(h, d):
    r = (d / 2)
    return (h - r) < h


# Calculating the arc radius

def obtainValues(values):
    d = []  # Distance
    disX = []  # Distance Cordenate Sol
    alt = []  # Height
    antdistancia = -50

    for pos in values:

        x, y = medides(pos)
        alt.append(y)

        if antdistancia != -50:
            d.append(x - antdistancia)
            disX.append(x)
        antdistancia = x

    return d, alt, disX


def medides(values):
    x = values[0]
    y = values[1]

    return x, y


# This method calculates the total costs.

def costsAque(n, alpha, beta, h, values):

    costosAltura = 0
    costosDistancia = 0
    esposible = True

    d, alt, disX = obtainValues(values)
    for i in range(0, n):

        costosAltura += (h - alt[i])

        if i < n - 1:
            costosDistancia += (d[i] ** 2)
            esposible = calc_impossible(h, d[i])
        elif esposible == False:
            break

    resultado = (alpha * costosAltura) + (beta * costosDistancia)

    return resultado
