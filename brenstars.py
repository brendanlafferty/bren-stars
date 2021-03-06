from typing import List
from math import gcd

import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


def find_m_from_n(n: int) -> int:
    """
    returns the smallest value that is co-prime with 4n and greater than n
    will either be n+1 or n+2 specifically the first odd number greater than n
    :param int n:
    :return:
    """
    odd = (n + 1) % 2
    if odd:
        return n+1
    else:
        return n+2

def construct_square(n: int) -> List[tuple]:
    """
    returns a list of the coordinate pairs for the location of 4n nodes arranged in a square.  The nodes will be
    connected elsewhere

    :param int n: order of brenstar to be created
    :return: list of the coordinate tuples of the square with side of length n

    """
    coordinates = [(0, 0)]
    # value points when moving up in axis values
    pos_movement_values = range(1, n + 1)
    # value points when moving down in axis values
    neg_movement_values = range(n-1, -1, -1)

    # create lists of length n for each side of the square
    y_axis_coordinates = list(zip([0] * n, pos_movement_values))
    x_at_max_y_coordinates = list(zip(pos_movement_values, [pos_movement_values[-1]] * n))
    y_at_max_x_coordinates = list(zip([pos_movement_values[-1]]*n, neg_movement_values))
    x_axis_coordinates = list(zip(neg_movement_values, [0] * n))

    # remove (0, 0) from the final side of the square
    del x_axis_coordinates[-1]

    # put all four sides together
    coordinates.extend(y_axis_coordinates)
    coordinates.extend(x_at_max_y_coordinates)
    coordinates.extend(y_at_max_x_coordinates)
    # one exception for the final side is for the n=1 case.  In that case x_axis_coordinates will be an empty list
    if x_axis_coordinates:
        coordinates.extend(x_axis_coordinates)

    return coordinates


def reorder_square_into_star(square_coords: List[tuple], co_factor: int, ind: int = None) -> List[tuple]:
    """
    reorders the coordinates of the nodes in a square to trace the path of the star given the coordinates, the co-factor
    The function is recursive.  The function doesn't create a true brenstar path unless the co-factor is the smallest
    co-prime factor of len(square_coords) that is greater than len(square_coords)/4.  The recursion ends when the
    coordinates (0, 0) are reached.  this mean that if the co-factor is not co-prime then not all of the coordinates
    passed will be returned in the list

    :param list(tuple) square_coords:
    :param int co_factor:
    :param int ind: recursive param
    :return: a list of coordinate tuples that start and end at (0,0)
    """

    if ind is None:
        ind = 0
    elif ind is 0:
        return [(0, 0)]
    next_ind = (ind + co_factor) % len(square_coords)
    star_coords = [square_coords[ind]]
    star_coords.extend(reorder_square_into_star(square_coords, co_factor, next_ind))
    return star_coords


def plot_coordinates(coordinates: List[tuple], axes: plt.Axes=None) -> plt.Axes:
    """
    Creates a line plot of a list of coordinates
    :param List[tuple] coordinates: list of coordinate tuples
    :param plt.Figure axes: optional can provide axes
    :return: None
    """
    if not axes:
        axes = plt.subplot(111)
    xs, ys = zip(*coordinates)
    plt.plot(xs, ys, '-', color='gold', marker='o', markerfacecolor='b')
    set_ticks_to_unit_spacing(axes)
    remove_border()
    return axes


def add_point_markers(n: int, axes: plt.Axes=None) -> plt.Axes:
    """
    adds points with integer coordinates to the plot to mimic the dot matrix paper that brenstars were first created on
    :param int n: Order of the brenstar
    :param plt.Axes axes: optional can provide axes
    :return:
    """
    if not axes:
        axes = plt.subplot(111)
    coordinates = ((x,y) for x in range(n+1) for y in range(n+1))
    xs, ys = zip(*coordinates)
    # TODO: create a function to determine whether the points are centrally interior, perephirally interior,
    #  intersection points on the star or vertices.  It would be called here to map the points to a color.
    plt.scatter(xs, ys, s=1, c='r', zorder=3)
    return axes


def set_ticks_to_unit_spacing(ax: plt.Axes, spacing_num: int = 1) -> None:
    """
    Sets the major tick spacing to units of the spacing number
    :param int spacing_num: spacing number
    :param plt.Axes ax: Axes object
    :return: None
    """
    ticker_loc = plticker.MultipleLocator(spacing_num)
    ax.xaxis.set_major_locator(ticker_loc)
    ax.yaxis.set_major_locator(ticker_loc)


def remove_border() -> None:
    """
    removes the border of the active plot
    :return: None
    """
    for spine in plt.gca().spines.values():
        spine.set_visible(False)


if __name__ == "__main__":
    fig = plt.figure(10, figsize=(9, 3.9), dpi=300)
    for n in range(1, 11):
        ax = plt.subplot(2, 5, n)
        ax.set_title(f'bren-star of order {n}', fontsize=8)
        m = find_m_from_n(n)
        sq_coords = construct_square(n)
        st_coords = reorder_square_into_star(sq_coords, m)
        add_point_markers(n, ax)
        plot_coordinates(st_coords, ax)
    fig.tight_layout()
    plt.savefig('brenstars1-10.png', transparent=True)
