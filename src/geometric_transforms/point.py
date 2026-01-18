import math


class Point:
    """
    Represents a 2D point with x and y coordinates.

    Supports arithmetic operations, distance calculations, and geometric utilities.

    Examples:
        p1 = Point(3, 4)
        p2 = Point(1, 2)

        p1 + p2          # Point(4, 6) - vector addition
        p1 - p2          # Point(2, 2) - vector subtraction
        p1 * 2           # Point(6, 8) - scalar multiplication
        -p1              # Point(-3, -4) - negation
        p1.magnitude()   # 5.0 - distance from origin
        p1.distance(p2)  # 2.828... - distance between points
        p1.dot(p2)       # 11 - dot product
        p1.angle()       # 53.13... degrees from positive x-axis
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __add__(self, other: "Point") -> "Point":
        """Vector addition: Point(1,2) + Point(3,4) = Point(4,6)"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> "Point":
        """Vector subtraction: Point(3,4) - Point(1,2) = Point(2,2)"""
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Point":
        """Scalar multiplication: Point(2,3) * 2 = Point(4,6)"""
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Point":
        """Allow scalar * Point: 2 * Point(2,3) = Point(4,6)"""
        return self * scalar

    def __neg__(self) -> "Point":
        """Negation: -Point(2,3) = Point(-2,-3)"""
        return Point(-self.x, -self.y)

    def __truediv__(self, scalar: float) -> "Point":
        """Scalar division: Point(4,6) / 2 = Point(2,3)"""
        return Point(self.x / scalar, self.y / scalar)

    def copy(self) -> "Point":
        """Return a copy of this point."""
        return Point(self.x, self.y)

    def to_tuple(self) -> tuple[float, float]:
        """Convert to tuple: Point(3,4).to_tuple() = (3, 4)"""
        return (self.x, self.y)

    @classmethod
    def from_tuple(cls, t: tuple[float, float]) -> "Point":
        """Create from tuple: Point.from_tuple((3, 4)) = Point(3, 4)"""
        return cls(t[0], t[1])

    def magnitude(self) -> float:
        """Distance from origin (vector length): Point(3,4).magnitude() = 5.0"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance(self, other: "Point") -> float:
        """Distance to another point: Point(0,0).distance(Point(3,4)) = 5.0"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dot(self, other: "Point") -> float:
        """Dot product: Point(1,2).dot(Point(3,4)) = 11"""
        return self.x * other.x + self.y * other.y

    def angle(self) -> float:
        """Angle in degrees from positive x-axis: Point(1,1).angle() = 45.0"""
        return math.degrees(math.atan2(self.y, self.x))

    def angle_to(self, other: "Point") -> float:
        """Angle in degrees from this point to another point."""
        diff = other - self
        return diff.angle()

    def normalize(self) -> "Point":
        """Return unit vector (magnitude 1) in same direction."""
        mag = self.magnitude()
        if mag == 0:
            return Point(0, 0)
        return self / mag

    def midpoint(self, other: "Point") -> "Point":
        """Midpoint between this point and another."""
        return (self + other) / 2

    def rotate_around(self, center: "Point", degrees: float) -> "Point":
        """Rotate this point around a center by given degrees (CCW positive)."""
        radians = math.radians(degrees)
        translated = self - center
        rotated_x = translated.x * math.cos(radians) - translated.y * math.sin(radians)
        rotated_y = translated.x * math.sin(radians) + translated.y * math.cos(radians)
        return Point(rotated_x, rotated_y) + center

    def reflect_over(self, line_point1: "Point", line_point2: "Point") -> "Point":
        """Reflect this point over the line defined by two points."""
        dx = line_point2.x - line_point1.x
        dy = line_point2.y - line_point1.y

        if dx == 0 and dy == 0:
            return self.copy()

        t = ((self.x - line_point1.x) * dx + (self.y - line_point1.y) * dy) / (dx * dx + dy * dy)
        closest_x = line_point1.x + t * dx
        closest_y = line_point1.y + t * dy

        return Point(2 * closest_x - self.x, 2 * closest_y - self.y)
