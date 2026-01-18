from ..point import Point


def reflect_x_axis(point: Point) -> Point:
    """
    Reflect a point over the x-axis.

    Args:
        point: The point to reflect

    Returns:
        A new Point reflected over y = 0
    """
    return Point(point.x, -point.y)


def reflect_y_axis(point: Point) -> Point:
    """
    Reflect a point over the y-axis.

    Args:
        point: The point to reflect

    Returns:
        A new Point reflected over x = 0
    """
    return Point(-point.x, point.y)


def reflect_horizontal_line(point: Point, y_value: float) -> Point:
    """
    Reflect a point over a horizontal line y = k.

    Args:
        point: The point to reflect
        y_value: The y-value of the horizontal line (k in y = k)

    Returns:
        A new Point reflected over y = y_value
    """
    # Distance from point to line
    distance = point.y - y_value
    # Reflect: go the same distance on the other side
    return Point(point.x, y_value - distance)


def reflect_vertical_line(point: Point, x_value: float) -> Point:
    """
    Reflect a point over a vertical line x = k.

    Args:
        point: The point to reflect
        x_value: The x-value of the vertical line (k in x = k)

    Returns:
        A new Point reflected over x = x_value
    """
    # Distance from point to line
    distance = point.x - x_value
    # Reflect: go the same distance on the other side
    return Point(x_value - distance, point.y)


def reflect_custom_line(point: Point, m: float, b: float) -> Point:
    """
    Reflect a point over a custom line y = mx + b.

    Args:
        point: The point to reflect
        m: The slope of the line
        b: The y-intercept of the line

    Returns:
        A new Point reflected over y = mx + b
    """
    # Direct reflection formula derived from:
    # 1. Find foot of perpendicular Q from point to line
    # 2. Reflected point = 2*Q - original point
    #
    # For point (x, y) over line y = mx + b:
    # x' = (x(1 - m²) + 2m(y - b)) / (1 + m²)
    # y' = (2mx + y(m² - 1) + 2b) / (1 + m²)

    m_squared = m * m
    denom = 1 + m_squared
    new_x = (point.x * (1 - m_squared) + 2 * m * (point.y - b)) / denom
    new_y = (2 * m * point.x + point.y * (m_squared - 1) + 2 * b) / denom

    return Point(new_x, new_y)