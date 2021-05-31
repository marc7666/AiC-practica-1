# ************************************
# Code made by:
# Aaron Arenas Tomás
# Marc Cervera Rosell
# ************************************
import math


def calc_impossible_pont(alt, distance_x, distance, height_aqueduct, pos_ant_x):
    """
    This method calculates the possibility of creating a bridge
    """

    radius = (distance / 2)
    height = math.sqrt((radius ** 2 - (
            (distance_x - pos_ant_x - radius) ** 2))
                       ) + (height_aqueduct - radius)
    return height > alt


def calc_impossible(alt, distance, height_aqueduct):
    """
    This method calculates the possibility of creating an aqueduct
    """

    radius = (distance / 2)
    height = (height_aqueduct - radius)
    return height > alt


def obtain_values(values):
    """This method obtains de three different values:
    the distance between two columns (d), the different heights (coordinates Y),
    the different coordinates X
    """

    distance = []  # Distance
    distance_x = []  # Distance Coordinate Sol
    alt = []  # Height
    ant_dis = -50

    for pos in values:

        coordinate_x, coordinate_y = measures(pos)
        alt.append(coordinate_y)
        distance_x.append(coordinate_x)
        if ant_dis != -50:
            distance.append(coordinate_x - ant_dis)

        ant_dis = coordinate_x

    return distance, alt, distance_x


def measures(values):
    """
    This method returns a tuple with a the two coordinates of a terrain point
    """

    coordinate_x = values[0]
    coordinate_y = values[1]

    return coordinate_x, coordinate_y


def costs_aqueduct(
        terrain_points, alpha, beta, height_aqueduct, alt, distance, index, costs_alt, costs_dis
):
    """
    This method calculates the costs of making an aqueduct
    """
    impossible = True

    if index == terrain_points:
        cost = (alpha * costs_alt) + (beta * costs_dis)
        return cost, impossible

    costs_alt += (height_aqueduct - alt[index])

    if 0 < index:
        impossible = calc_impossible(alt[index], distance[index - 1], height_aqueduct)

    if index < terrain_points - 1:
        costs_dis += (distance[index] ** 2)

    if not impossible:
        cost = 0
        return cost, impossible

    return costs_aqueduct(
        terrain_points, alpha, beta, height_aqueduct, alt, distance, index + 1, costs_alt, costs_dis
    )


def cost_pont(terrain_points, height_aqueduct, alt, distance_x, index):
    """
    This method calculates the costs of making a bridge
    """
    impossible = True

    if index == terrain_points:
        return impossible
    d_pont = distance_x[terrain_points - 1] - distance_x[0]
    if 0 < index:
        impossible = calc_impossible_pont(
            alt[index], distance_x[index], d_pont, height_aqueduct, distance_x[0]
        )

    if not impossible:
        return impossible

    return cost_pont(terrain_points, height_aqueduct, alt, distance_x, index + 1)


def calculate(terrain_points, alpha, beta, height_aqueduct, values):
    """
    This method will calculate the possibility of making a bridge and 
    making an aqueduct and will return the best one  of the possibilities
    """
    distance, alt, distance_x = obtain_values(values)
    index = 0
    costs_alt = 0
    costs_dis = 0
    """Calculate cost pont"""
    costs_alt_pont = (height_aqueduct - alt[0]) + (height_aqueduct - alt[terrain_points - 1])
    d_pont = distance_x[terrain_points - 1] - distance_x[0]
    cost = ((alpha * costs_alt_pont) + (beta * (d_pont ** 2)))

    if terrain_points == 2:
        cost2, impossible = costs_aqueduct(
            terrain_points, alpha, beta, height_aqueduct, alt, distance, index, costs_alt, costs_dis
        )
        if impossible:
            return cost2
        else:
            return "impossible"
    else:
        impossiblePont = cost_pont(terrain_points, height_aqueduct, alt, distance_x, index)
        index = 0
        cost2, impossible = costs_aqueduct(
            terrain_points, alpha, beta, height_aqueduct, alt, distance, index, costs_alt, costs_dis
        )
    if impossiblePont and not impossible:
        return cost

    elif impossible and not impossiblePont:
        return cost2

    elif cost < cost2 and impossible and impossiblePont:
        return cost

    elif cost > cost2 and impossible and impossiblePont:
        return cost2
    return "impossible"
