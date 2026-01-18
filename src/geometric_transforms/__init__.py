"""
Geometric Transforms - A library for 2D point transformations.

This package provides a Point class and transformation functions for:
- Translation
- Rotation (90°, 180°, 270°, custom angles)
- Reflection (over axes, lines)
- Dilation (scaling)

Example:
    from geometric_transforms import Point, translate, rotate_90

    p = Point(3, 4)
    p_translated = translate(p, 1, 2)  # Point(4, 6)
    p_rotated = rotate_90(p, Point(0, 0))  # Point(-4, 3)
"""

from .point import Point
from .transforms import (
    translate,
    rotate_90,
    rotate_180,
    rotate_270,
    rotate_custom,
    reflect_x_axis,
    reflect_y_axis,
    reflect_horizontal_line,
    reflect_vertical_line,
    reflect_custom_line,
    dilate,
)

__version__ = "0.1.0"
__all__ = [
    "Point",
    "translate",
    "rotate_90",
    "rotate_180",
    "rotate_270",
    "rotate_custom",
    "reflect_x_axis",
    "reflect_y_axis",
    "reflect_horizontal_line",
    "reflect_vertical_line",
    "reflect_custom_line",
    "dilate",
]
