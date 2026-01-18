# Transformations Project - Development Instructions

> **AI-Generated Project**: This codebase was developed with assistance from Claude (Anthropic). These instructions document the requirements and specifications used during development.

## Overview

This project is a pip-installable Python library for geometric transformations that applies translation, rotation, reflection, and dilation to 2D points.

---

## Point Class Requirements

The `Point` class in `src/geometric_transforms/point.py` provides significant value beyond simple tuples:

### Required Operations
- **Arithmetic**: `+`, `-`, `*`, `/`, unary `-` (negation)
- **Distance methods**: `magnitude()` (from origin), `distance(other)`
- **Angle methods**: `angle()` (from positive x-axis), `angle_to(other)`
- **Utilities**: `dot()`, `normalize()`, `midpoint()`, `copy()`
- **Conversion**: `to_tuple()`, `from_tuple()`
- **Built-in transforms**: `rotate_around(center, degrees)`, `reflect_over(point1, point2)`

### Documentation
The class docstring includes usage examples showing the value of each operation.

---

## Reflection Function Requirements

### Formula
The `reflect_custom_line(point, m, b)` function uses the correct reflection formula.
For point (x, y) over line y = mx + b:
```
x' = (x(1 - m²) + 2m(y - b)) / (1 + m²)
y' = (2mx + y(m² - 1) + 2b) / (1 + m²)
```

### Optimization
- Precompute repeated values like `m²` and denominators
- No debug print statements

---

## Rotation Function Requirements

### Math Comments
The `rotate_custom` function includes comments explaining:
1. Degrees to radians conversion (trig functions use radians)
2. The rotation matrix formula:
   ```
   [cos(θ) -sin(θ)] [x]   [x*cos(θ) - y*sin(θ)]
   [sin(θ)  cos(θ)] [y] = [x*sin(θ) + y*cos(θ)]
   ```
3. The translate-rotate-translate pattern

---

## CLI Example Features

The example CLI in `examples/` provides:

### Input Mode Menu System
1. **Single Point** - User enters one x, y coordinate pair
2. **Multiple Points (Inline)** - Format: `x1, y1, x2, y2, ...` (comma or space separated)
3. **CSV File Import** - Flexible protocol with:
   - Auto-detect headers
   - Column selection UI
   - Error reporting for skipped rows

### Transformation Loop
After each transformation:
1. Apply another transformation to current results
2. Start over with new points
3. Exit program

Additional features:
- Transformation count tracking
- CSV export option for multi-point results

---

## Code Style

- Type hints for function parameters and return values
- Docstrings with Args and Returns sections
- Single-purpose functions
- Minimal over-engineering

---

## File Structure

```
geometric-transforms/
├── src/
│   └── geometric_transforms/
│       ├── __init__.py          # Package exports
│       ├── point.py             # Point class
│       └── transforms/
│           ├── __init__.py
│           ├── translation.py
│           ├── rotation.py
│           ├── reflection.py
│           └── dilation.py
├── examples/
│   ├── cli.py                   # Interactive CLI
│   ├── ui.py                    # CLI utilities
│   ├── example_simple.csv
│   ├── example_with_labels.csv
│   └── example_no_header.csv
├── pyproject.toml               # Package configuration
├── README.md                    # User documentation
├── LICENSE                      # MIT License
├── .gitignore
└── CLAUDE.md                    # This file
```
