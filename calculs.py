# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import math

# distance_x todas las posiciones del vector
# posant_x siempre el eje x_1

'''
This method calculates the possibility of creating a bridge
'''


def calc_impossible_pont(alt, distance_x, distance, height_aqueduct, posant_x):
    radius = (distance / 2)
    height = math.sqrt((radius ** 2 - (
            (distance_x - posant_x - radius) ** 2))
                        ) + (height_aqueduct - radius)
    return height > alt


'''
This method calculates the possiblity of creating an aqueduct
'''


def calc_impossible(alt, distance, height_aqueduct):
    radius = (distance / 2)
    height = (height_aqueduct - radius)
    return height > alt


'''This method obtains de three different values: the distance between two columns (d), the different heights (
coordinates Y), the different coordinates X 
'''


def obtain_values(values):
    distance = []  # Distance
    distance_x = []  # Distance Cordenate Sol
    alt = []  # Height
    ant_dis = -50

    for pos in values:

        coordinate_x, coordinate_y = medides(pos)
        alt.append(coordinate_y)
        distance_x.append(coordinate_x)
        if ant_dis != -50:
            distance.append(coordinate_x - ant_dis)

        ant_dis = coordinate_x

    return distance, alt, distance_x


'''
This method returns a tuple with a the two coordinates of a terrain point
'''


def medides(values):
    coordinate_x = values[0]
    coordinate_y = values[1]

    return coordinate_x, coordinate_y


'''
This method calculates the costs of making an aqueduct
'''


def costs_aqueduct(terrain_points, alpha, beta, height_aqueduct, alt, distance):
    costs_alt = 0
    costs_dis = 0
    impossible = True

    for i in range(0, terrain_points):
        costs_alt += (height_aqueduct - alt[i])
        if 0 < i:
            impossible = calc_impossible(alt[i], distance[i - 1], height_aqueduct)
        if i < terrain_points - 1:
            costs_dis += (distance[i] ** 2)
        if not impossible:
            break

    cost = (alpha * costs_alt) + (beta * costs_dis)

    return cost, impossible


'''
This method calculates the costs of making a bridge
'''


def cost_pont(terrain_points, alpha, beta, height_aqueduct, alt, distance_x):
    costs_alt_pont = (height_aqueduct - alt[0]) + (
            height_aqueduct - alt[terrain_points - 1]
    )
    d_pont = distance_x[terrain_points - 1] - distance_x[0]
    impossible = True

    for i in range(0, terrain_points):

        if 0 < i:
            impossible = calc_impossible_pont(
                alt[i], distance_x[i], d_pont, height_aqueduct, distance_x[0]
            )

        if not impossible:
            break

    cost = ((alpha * costs_alt_pont) + (beta * (d_pont ** 2)))

    return cost, impossible


'''
This method will calculate the possibility of making a bridge and making an aqueduct and will return the best one 
of the possiblities
'''


def calculate(terrain_points, alpha, beta, height_aqueduct, values):
    distance, alt, distance_x = obtain_values(values)
    if terrain_points == 2:
        cost2, impossible = costs_aqueduct(
            terrain_points, alpha, beta, height_aqueduct, alt, distance
        )
        if impossible:
            return cost2
        return "impossible"
    else:
        cost1, impossible_pont = cost_pont(
            terrain_points, alpha, beta, height_aqueduct, alt, distance_x
        )
        cost2, impossible = costs_aqueduct(
            terrain_points, alpha, beta, height_aqueduct, alt, distance
        )

    if impossible_pont and not impossible:
        return cost1

    elif impossible and not impossible_pont:
        return cost2

    elif cost1 < cost2 and impossible and impossible_pont:
        return cost1

    elif cost1 > cost2 and impossible and impossible_pont:
        return cost2
    return "impossible"
