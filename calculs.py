# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import math

# distanceX todas las posiciones del vector
# posantX siempre el eje x_1

'''
This method calculates the possibility of creating a bridge
'''


def calc_impossiblepont(alt, distanceX, distance, heightAqueduct, posantX):
    radius = (distance / 2)
    height = math.sqrt((radius ** 2 - ((distanceX - posantX - radius) ** 2))) + (heightAqueduct - radius)
    return height > alt


'''
This method calculates the possiblity of creating an aqueduct
'''


def calc_impossible(alt, distance, heightAqueduct):
    radius = (distance / 2)
    height = (heightAqueduct - radius)
    return height > alt


'''This method obtains de three different values: the distance between two columns (d), the different heights (
coordinates Y), the different coordinates X 
'''


def obtainValues(values):
    distance = []  # Distance
    distanceX = []  # Distance Cordenate Sol
    alt = []  # Height
    antDis = -50

    for pos in values:

        coordinateX, coordinateY = medides(pos)
        alt.append(coordinateY)
        distanceX.append(coordinateX)
        if antDis != -50:
            distance.append(coordinateX - antDis)

        antDis = coordinateX

    return distance, alt, distanceX


'''
This method returns a tuple with a the two coordinates of a terrain point
'''


def medides(values):
    coordinateX = values[0]
    coordinateY = values[1]

    return coordinateX, coordinateY


'''
This method calculates the costs of making an aqueduct
'''


def costsAque(terrainPoints, alpha, beta, heightAqueduct, alt, distance):
    costsAlt = 0
    costsDis = 0
    impossible = True

    for i in range(0, terrainPoints):
        costsAlt += (heightAqueduct - alt[i])
        if 0 < i:
            impossible = calc_impossible(alt[i], distance[i - 1], heightAqueduct)
        if i < terrainPoints - 1:
            costsDis += (distance[i] ** 2)
        if not impossible:
            break

    cost = (alpha * costsAlt) + (beta * costsDis)

    return cost, impossible


'''
This method calculates the costs of making a bridge
'''


def costPont(terrainPoints, alpha, beta, heightAqueduct, alt, distanceX):
    costsAltPont = (heightAqueduct - alt[0]) + (heightAqueduct - alt[terrainPoints - 1])
    dPont = distanceX[terrainPoints - 1] - distanceX[0]
    impossible = True

    for i in range(0, terrainPoints):

        if 0 < i:
            impossible = calc_impossiblepont(alt[i], distanceX[i], dPont, heightAqueduct, distanceX[0])

        if not impossible:
            break

    cost = ((alpha * costsAltPont) + (beta * (dPont ** 2)))

    return cost, impossible


'''
This method will calculate the possibility of making a bridge and making an aqueduct and will return the best one 
of the possiblities
'''


def calculate(terrainPoints, alpha, beta, heightAqueduct, values):
    distance, alt, distanceX = obtainValues(values)
    if terrainPoints == 2:
        cost2, impossible = costsAque(terrainPoints, alpha, beta, heightAqueduct, alt, distance)
        if impossible:
            return cost2
        else:
            return "impossible"
    else:
        cost1, impossiblePont = costPont(terrainPoints, alpha, beta, heightAqueduct, alt, distanceX)
        cost2, impossible = costsAque(terrainPoints, alpha, beta, heightAqueduct, alt, distance)

    if impossiblePont and not impossible:
        return cost1

    elif impossible and not impossiblePont:
        return cost2

    elif cost1 < cost2 and impossible and impossiblePont:
        return cost1

    elif cost1 > cost2 and impossible and impossiblePont:
        return cost2
    return "impossible"
