# Geometric Transforms

A Python library for 2D geometric point transformations.

> **Note**: This project was generated with assistance from Claude (AI). See [CLAUDE.md](CLAUDE.md) for development instructions used during creation.

## Installation

```bash
pip install geometric-transforms
```

Or install from source:

```bash
git clone https://github.com/saahir/geometric-transforms.git
cd geometric-transforms
pip install .
```

## Features

### Point Class

A feature-rich 2D point class with:

- **Arithmetic**: `+`, `-`, `*`, `/`, unary `-`
- **Distance**: `magnitude()`, `distance(other)`
- **Angles**: `angle()`, `angle_to(other)`
- **Utilities**: `dot()`, `normalize()`, `midpoint()`, `copy()`
- **Conversion**: `to_tuple()`, `from_tuple()`
- **Built-in transforms**: `rotate_around()`, `reflect_over()`

### Transformations

- **Translation**: Move points by (dx, dy)
- **Rotation**: 90°, 180°, 270°, or custom angles around any center
- **Reflection**: Over x-axis, y-axis, horizontal/vertical lines, or custom lines (y = mx + b)
- **Dilation**: Scale from any center point

## Usage

```python
from geometric_transforms import Point, translate, rotate_90, reflect_x_axis, dilate

# Create a point
p = Point(3, 4)
print(p.magnitude())  # 5.0

# Translate
p2 = translate(p, 1, 2)  # Point(4, 6)

# Rotate 90° counterclockwise around origin
p3 = rotate_90(p, Point(0, 0))  # Point(-4, 3)

# Reflect over x-axis
p4 = reflect_x_axis(p)  # Point(3, -4)

# Dilate by factor 2 from origin
p5 = dilate(p, Point(0, 0), 2)  # Point(6, 8)

# Point arithmetic
a = Point(1, 2)
b = Point(3, 4)
print(a + b)  # Point(4, 6)
print(a.dot(b))  # 11
print(a.distance(b))  # 2.828...
```

## Example CLI

An interactive CLI is included in the `examples/` directory:

```bash
cd examples
python cli.py
```

Features:
- Single point, multiple points, or CSV file input
- Apply multiple transformations in sequence
- Export results to CSV

## API Reference

### Point Class

```python
Point(x: float, y: float)
```

Methods:
- `magnitude()` - Distance from origin
- `distance(other)` - Distance to another point
- `angle()` - Angle in degrees from positive x-axis
- `angle_to(other)` - Angle to another point
- `dot(other)` - Dot product
- `normalize()` - Unit vector in same direction
- `midpoint(other)` - Midpoint between two points
- `copy()` - Create a copy
- `to_tuple()` - Convert to (x, y) tuple
- `from_tuple(t)` - Create from tuple (class method)
- `rotate_around(center, degrees)` - Rotate around a point
- `reflect_over(p1, p2)` - Reflect over line defined by two points

### Transform Functions

```python
translate(point, dx, dy) -> Point
rotate_90(point, center) -> Point
rotate_180(point, center) -> Point
rotate_270(point, center) -> Point
rotate_custom(point, center, degrees) -> Point
reflect_x_axis(point) -> Point
reflect_y_axis(point) -> Point
reflect_horizontal_line(point, y_value) -> Point
reflect_vertical_line(point, x_value) -> Point
reflect_custom_line(point, m, b) -> Point  # y = mx + b
dilate(point, center, scale) -> Point
```

## License

MIT License - see [LICENSE](LICENSE)
