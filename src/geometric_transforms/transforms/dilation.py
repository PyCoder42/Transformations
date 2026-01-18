from ..point import Point


def dilate(point: Point, center: Point, scale: float) -> Point:
    """
    Dilate a point from a center by a scale factor.

    Args:
        point: The point to dilate
        center: The center of dilation
        scale: The scale factor (>1 enlarges, <1 shrinks, negative inverts)

    Returns:
        A new Point with the dilated coordinates
    """
    # Vector from center to point
    dx = point.x - center.x
    dy = point.y - center.y

    # Scale the vector
    new_x = center.x + dx * scale
    new_y = center.y + dy * scale

    return Point(new_x, new_y)
