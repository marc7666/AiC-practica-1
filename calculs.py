# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************

import math


# Calculating the arc radius

def radius(values):

    rad = []
    dis = []
    alt = []
    antdistancia = 0

    for pos in values:

        int1, int2 = medides(pos)
        rad.append(math.sqrt(int1 ** 2 + int2 ** 2))
        alt.append(int2)

        if antdistancia != 0:
         dis.append(int1-antdistancia)

        antdistancia = int1

    return rad, dis, alt

def medides(values):

    int1 = values[0]
    int2 = values[1]

    return int1, int2

def costos(n, alpha, beta, h, dis, alt):

    costosAltura = 0
    costosDistancia = 0

    for i in range(0, n):

        costosAltura += alpha*(h-alt[i])
        if i < n-1:
            costosDistancia += (beta*(dis[i]**2))

    resultado = costosAltura + costosDistancia

    return resultado