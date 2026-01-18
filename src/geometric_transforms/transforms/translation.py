from ..point import Point


def translate(point: Point, dx: float, dy: float) -> Point:
    """
    Translate a point by (dx, dy).

    Args:
        point: The original point
        dx: Horizontal translation (positive = right)
        dy: Vertical translation (positive = up)

    Returns:
        A new Point with the translated coordinates
    """
    return Point(point.x + dx, point.y + dy)
