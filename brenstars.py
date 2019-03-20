from typing import List
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker


_ticker_loc = plticker.MultipleLocator(1)


def construct_square(n: int) -> List[tuple]:
    """
    returns a list of the coordinate pairs for the location of 4n nodes aranged in a square.  The nodes will be
    connected elsewhere

    :param int n: order of brenstar to be created
    :return: list of the coordinate tuples of the square with side of length n

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


def set_ticks_to_unit_spacing(ax: plt.Axes) -> None:
    """
    Sets the major tick spacing to units of 1
    :param plt.Axes ax: Axes object
    :return: None
    """
    ax.xaxis.set_major_locator(_ticker_loc)
    ax.yaxis.set_major_locator(_ticker_loc)


def remove_border() -> None:
    """
    removes the border of the active plot
    :return: None
    """
    for spine in plt.gca().spines.values():
        spine.set_visible(False)


if __name__ == "__main__":

    n = 3
    m = 5
    sq_coords = construct_square(n)
    print(sq_coords)
    st_coords = reorder_square_into_star(sq_coords, m)
    print(st_coords)
    plot_coordinates(st_coords)
    plt.show()
