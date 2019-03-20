from typing import List
import matplotlib.pyplot as plt


def construct_square(n: int) -> List[tuple]:
    """
    returns a list of the coordinate pairs for the location of 4n nodes aranged in a square.  The nodes will be
    connected elsewhere

    :param int n: order of brenstar to be created
    :return:

    """
    coordinates = [(0, 0)]
    # value points when moving up in axis values
    pos_movement_values = range(1, n + 1)
    # value points when moving down in axis values
    neg_movement_values = range(n-1, -1, -1)

    y_axis_coordinates = list(zip([0] * n, pos_movement_values))
    x_at_max_y_coordinates = list(zip(pos_movement_values, [pos_movement_values[-1]] * n))
    y_at_max_x_coordinates = list(zip([pos_movement_values[-1]]*n, neg_movement_values))
    x_axis_coordinates = list(zip(neg_movement_values, [0] * n))
    del x_axis_coordinates[-1]  # remove(0, 0)]

    coordinates.extend(y_axis_coordinates)
    coordinates.extend(x_at_max_y_coordinates)
    coordinates.extend(y_at_max_x_coordinates)
    if x_axis_coordinates:
        coordinates.extend(x_axis_coordinates)

    return coordinates


def reorder_square_into_star(square_coords: List[tuple], co_factor: int, ind: int = None) -> List[tuple]:
    """
    reorders the coordinates of the nodes in a square to trace the path of the star given the coordinates, the co-factor
    The function is recursive.  The function doesn't create a true brenstar path unless the co-factor is the smallest
    co-prime factor of len(square_coords) that is greater than len(square_coords)/4
    :param list(tuple) square_coords:
    :param int co_factor:
    :param int ind: recursive param
    :return:
    """

    if ind is None:
        ind = 0
    elif ind is 0:
        return [(0, 0)]
    next_ind = (ind + co_factor) % len(square_coords)
    star_coords = [square_coords[ind]]
    star_coords.extend(reorder_square_into_star(square_coords, co_factor, next_ind))
    return star_coords


if __name__ == "__main__":

    n = 2
    m = 3
    sq_coords = construct_square(n)
    print(sq_coords)
    st_coords = reorder_square_into_star(sq_coords, m)
    print(st_coords)
