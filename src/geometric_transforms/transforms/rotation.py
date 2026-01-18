import math
from ..point import Point


def rotate_90(point: Point, center: Point) -> Point:
    """
    Rotate a point 90 degrees counterclockwise around a center point.

    Args:
        point: The point to rotate
        center: The center of rotation

    Returns:
        A new Point with the rotated coordinates
    """
    # Translate to origin
    temp_x = point.x - center.x
    temp_y = point.y - center.y

    # Rotate 90 degrees CCW: (x, y) -> (-y, x)
    rotated_x = -temp_y
    rotated_y = temp_x

    # Translate back
    return Point(rotated_x + center.x, rotated_y + center.y)


def rotate_180(point: Point, center: Point) -> Point:
    """
    Rotate a point 180 degrees around a center point.

    Args:
        point: The point to rotate
        center: The center of rotation

    Returns:
        A new Point with the rotated coordinates
    """
    # Translate to origin
    temp_x = point.x - center.x
    temp_y = point.y - center.y

    # Rotate 180 degrees: (x, y) -> (-x, -y)
    rotated_x = -temp_x
    rotated_y = -temp_y

    # Translate back
    return Point(rotated_x + center.x, rotated_y + center.y)


def rotate_270(point: Point, center: Point) -> Point:
    """
    Rotate a point 270 degrees counterclockwise (90 degrees clockwise) around a center point.

    Args:
        point: The point to rotate
        center: The center of rotation

    Returns:
        A new Point with the rotated coordinates
    """
    # Translate to origin
    temp_x = point.x - center.x
    temp_y = point.y - center.y

    # Rotate 270 degrees CCW (90 CW): (x, y) -> (y, -x)
    rotated_x = temp_y
    rotated_y = -temp_x

    # Translate back
    return Point(rotated_x + center.x, rotated_y + center.y)


def rotate_custom(point: Point, center: Point, degrees: float) -> Point:
    """
    Rotate a point by any angle around a center point.

    Args:
        point: The point to rotate
        center: The center of rotation
        degrees: The angle in degrees (positive = counterclockwise)

    Returns:
        A new Point with the rotated coordinates
    """
    
    # Convert degrees to radians (trig functions use radians)
    radians = math.radians(degrees)

    # Translate the point to the origin (relative to center)
    temp_x = point.x - center.x
    temp_y = point.y - center.y

    # Apply rotation matrix: [cos(θ) -sin(θ)] [x]   [x*cos(θ) - y*sin(θ)]
    #                        [sin(θ)  cos(θ)] [y] = [x*sin(θ) + y*cos(θ)]
    cos_theta = math.cos(radians)
    sin_theta = math.sin(radians)
    rotated_x = temp_x * cos_theta - temp_y * sin_theta
    rotated_y = temp_x * sin_theta + temp_y * cos_theta

    # Translate the point back to the original position
    return Point(rotated_x + center.x, rotated_y + center.y)
