# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import math


# Calculating posibility create pont
# disx todas las posiciones del vector
# posantX siempre el eje x_1

def calc_impossiblepont(alt, disX, d, h, posantX):
    r = (d / 2)
    height = math.sqrt((r ** 2 - ((disX - posantX - r) ** 2))) + (h - r)
    return height > alt


# Calculating posibility create aqueduct
def calc_impossible(alt, d, h):
    r = (d / 2)
    height = (h - r)
    return height > alt



def obtainValues(values):
    d = []  # Distance
    disX = []  # Distance Cordenate Sol
    alt = []  # Height
    antDis = -50

    for pos in values:

        x, y = medides(pos)
        alt.append(y)
        disX.append(x)
        if antDis != -50:
            d.append(x - antDis)

        antDis = x

    return d, alt, disX


def medides(values):
    x = values[0]
    y = values[1]

    return x, y


# This method calculates the total costs.
def costsAque(n, alpha, beta, h, alt, d, index, costsAlt, costsDis):

    impossible = True

    if index == n:
        cost = (alpha * costsAlt) + (beta * costsDis)
        return cost, impossible

    costsAlt += (h - alt[index])

    if 0 < index:
        impossible = calc_impossible(alt[index], d[index - 1], h)

    if index < n - 1:
        costsDis += (d[index] ** 2)

    if not impossible:
        cost = 0
        return cost, impossible

    return costsAque(n, alpha, beta, h, alt, d, index + 1, costsAlt, costsDis)



# This method calculates the total costs.
def costPont(n, h, alt, disX, index):

    impossible = True

    if index == n:
        return impossible
    dPont = disX[n - 1] - disX[0]
    if 0 < index:
        impossible = calc_impossiblepont(alt[index], disX[index], dPont, h, disX[0])

    if not impossible:
        return impossible

    return costPont(n, h, alt, disX, index + 1)


def calculate(n, alpha, beta, h, values):
    # values
    d, alt, disX = obtainValues(values)
    index = 0
    costsAlt = 0
    costsDis = 0
    # Calcul cost pont
    costsAltPont = (h - alt[0]) + (h - alt[n - 1])
    dPont = disX[n - 1] - disX[0]
    cost = ((alpha * costsAltPont) + (beta * (dPont ** 2)))

    if n == 2:
        cost2, impossible = costsAque(n, alpha, beta, h, alt, d, index, costsAlt, costsDis)
        if impossible:
            return cost2
        else:
            return "impossible"
    else:
        impossiblePont = costPont(n, h, alt, disX, index)
        index = 0
        cost2, impossible = costsAque(n, alpha, beta, h, alt, d, index, costsAlt, costsDis)
    impossible = True
    if impossiblePont and not impossible:
        return cost

    elif impossible and not impossiblePont:
        return cost2

    elif cost < cost2 and impossible and impossiblePont:
        return cost

    elif cost > cost2 and impossible and impossiblePont:
        return cost2
    return "impossible"
