# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math


# Calculating posibility create pont
def calc_impossiblepont(disX, d, h, posantX):
    r = (d / 2)
    height = math.sqrt((r ** 2 - ((disX - posantX - r) ** 2))) + h
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
        disX.append(x)
        if antdistancia != -50:
            d.append(x - antdistancia)

        antdistancia = x

    return d, alt, disX


def medides(values):
    x = values[0]
    y = values[1]

    return x, y


# This method calculates the total costs.

def costsAque(n, alpha, beta, h, values):
    costosaltura = 0
    costosdistancia = 0
    impossible = True

    d, alt, disX = obtainValues(values)
    for i in range(0, n):
        costosaltura += (h - alt[i])

        if i < n - 1:
            costosdistancia += (d[i] ** 2)
            impossible = calc_impossible(h, d[i])
        elif not impossible:
            break

    cost = (alpha * costosaltura) + (beta * costosdistancia)
    print(impossible)
    return cost


# This method calculates the total costs.

def costPont(n, alpha, beta, h, values):

    d, alt, disX = obtainValues(values)

    costosaltura = (h - alt[0]) + (h - alt[n - 1])
    dPont = disX[n - 1] - disX[0]
    impossible = True

    for i in range(0, n):
        if 0 < i < n-1:
            impossible = calc_impossiblepont(disX[i], dPont, h, disX[0])
        elif not impossible:
            break

    cost = (alpha * costosaltura) + (beta * (dPont ** 2))
    print(impossible)
    print(dPont)
    return cost
