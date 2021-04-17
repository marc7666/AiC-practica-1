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
    height = (h-r)
    return height >= alt

# Calculating the arc radius
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
def costsAque(n, alpha, beta, h, alt, d):
    costsAlt = 0
    costsDis = 0
    impossible = True

    for i in range(0, n):
        costsAlt += (h - alt[i])
        if 0 < i:
            impossible = calc_impossible(alt[i], d[i - 1], h)
        if i < n - 1:
            costsDis += (d[i] ** 2)
        if not impossible:
            break

    cost = (alpha * costsAlt) + (beta * costsDis)

    return cost, impossible

# This method calculates the total costs.
def costPont(n, alpha, beta, h, alt, disX, d):

    costsAltPont = (h - alt[0]) + (h - alt[n - 1])
    dPont = disX[n - 1] - disX[0]
    impossible = True

    for i in range(0, n):

        if 0 < i:
            impossible = calc_impossiblepont(alt[i], disX[i], dPont, h, disX[0])

        if not impossible:
            break

    cost = ((alpha * costsAltPont) + (beta * (dPont ** 2)))

    return cost, impossible


def calculate(n, alpha, beta, h, values):

    d, alt, disX = obtainValues(values)
    if n == 2:
        cost2, impossible = costsAque(n, alpha, beta, h, alt, d)
        if impossible:
            return cost2
        else:
            return "impossible"
    else:
        cost1, impossiblePont = costPont(n, alpha, beta, h, alt, disX, d)
        cost2, impossible = costsAque(n, alpha, beta, h, alt, d)

    if impossiblePont and not impossible:
        return cost1

    elif impossible and not impossiblePont:
        return cost2

    elif cost1 < cost2 and impossible and impossiblePont:
        return cost1

    elif cost1 > cost2 and impossible and impossiblePont:
        return cost2
    return "impossible"
