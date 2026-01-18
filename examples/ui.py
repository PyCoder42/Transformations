import csv
from geometric_transforms import Point


def print_header(title: str) -> None:
    """Print a formatted header."""
    print("\n" + "=" * 40)
    print(f"  {title}")
    print("=" * 40)


def print_menu(options: list[str]) -> None:
    """Print a numbered menu of options."""
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print()


def get_menu_choice(prompt: str, num_options: int) -> int:
    """Get a valid menu choice from the user."""
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= num_options:
                return choice
            print(f"Please enter a number between 1 and {num_options}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float(prompt: str) -> float:
    """Get a float value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_point(prompt: str = "Enter point") -> Point:
    """Get a point from the user."""
    print(prompt)
    x = get_float("  x: ")
    y = get_float("  y: ")
    return Point(x, y)


def get_center_point() -> Point:
    """Get a center point, with option for origin or custom."""
    print("\nCenter Point:")
    print_menu(["Origin (0, 0)", "Custom point"])
    choice = get_menu_choice("Select center: ", 2)

    if choice == 1:
        return Point(0, 0)
    else:
        return get_point("Enter custom center point:")


def display_result(original: Point, transformed: Point, description: str) -> None:
    """Display the transformation result."""
    print("\n" + "-" * 40)
    print(f"  {description}")
    print(f"  Original:    {original}")
    print(f"  Transformed: {transformed}")
    print("-" * 40)


def confirm_continue() -> bool:
    """Ask if user wants to perform another transformation."""
    print("\nPerform another transformation?")
    print_menu(["Yes", "No"])
    return get_menu_choice("Select: ", 2) == 1


def get_input_mode() -> int:
    """Get the input mode from the user."""
    print("\nHow would you like to input points?")
    print_menu([
        "Single point",
        "Multiple points (inline)",
        "CSV file",
    ])
    return get_menu_choice("Select input mode: ", 3)


def get_multiple_points() -> list[Point]:
    """
    Get multiple points from inline input.

    Format: x1, y1, x2, y2, ... (comma or space separated)
    """
    print("\nEnter points as: x1, y1, x2, y2, x3, y3, ...")
    print("(You can use commas or spaces as separators)")

    while True:
        raw = input("Points: ").strip()
        # Replace commas with spaces, then split on whitespace
        values = raw.replace(",", " ").split()

        if len(values) < 2:
            print("Please enter at least one point (x, y pair).")
            continue

        if len(values) % 2 != 0:
            print("Error: Odd number of values. Each point needs x and y.")
            continue

        try:
            floats = [float(v) for v in values]
            points = []
            for i in range(0, len(floats), 2):
                points.append(Point(floats[i], floats[i + 1]))
            print(f"  Parsed {len(points)} point(s): {points}")
            return points
        except ValueError:
            print("Error: Could not parse numbers. Please use valid numbers.")


def get_csv_points() -> list[Point]:
    """
    Read points from a CSV file with flexible column selection.

    Protocol:
    1. User provides CSV file path
    2. Show available columns
    3. User selects which columns contain x and y coordinates
    4. Parse and return points
    """
    print("\n--- CSV Import ---")
    print("Your CSV should have columns containing x and y coordinates.")

    while True:
        filepath = input("Enter CSV file path: ").strip()
        if not filepath:
            print("Please enter a file path.")
            continue

        try:
            # First pass: read only first row to detect headers and column count
            with open(filepath, "r", newline="") as f:
                reader = csv.reader(f)
                first_row = next(reader, None)

            if first_row is None:
                print("Error: CSV file is empty.")
                continue

            # Check if first row looks like a header (check first two columns only)
            has_header = False
            try:
                float(first_row[0])
                float(first_row[1])
            except (ValueError, IndexError):
                has_header = True

            if has_header:
                headers = first_row
                print(f"\nDetected header row with {len(headers)} columns:")
                for i, h in enumerate(headers):
                    print(f"  {i + 1}. {h}")
            else:
                headers = [f"Column {i + 1}" for i in range(len(first_row))]
                print(f"\nNo header detected. Found {len(headers)} columns:")
                for i, h in enumerate(headers):
                    print(f"  {i + 1}. {h}")

            if len(headers) < 2:
                print("Error: Need at least 2 columns for x and y.")
                continue

            # Get column selections
            print()
            x_col = get_menu_choice("Select column for X coordinates: ", len(headers)) - 1
            y_col = get_menu_choice("Select column for Y coordinates: ", len(headers)) - 1

            if x_col == y_col:
                print("Error: X and Y columns must be different.")
                continue

            # Second pass: stream rows and parse points
            points = []
            errors = []
            with open(filepath, "r", newline="") as f:
                reader = csv.reader(f)
                if has_header:
                    next(reader)  # Skip header row
                    start_row = 2
                else:
                    start_row = 1

                for row_num, row in enumerate(reader, start=start_row):
                    if len(row) <= max(x_col, y_col):
                        errors.append(f"Row {row_num}: Not enough columns")
                        continue
                    try:
                        x = float(row[x_col])
                        y = float(row[y_col])
                        points.append(Point(x, y))
                    except ValueError:
                        errors.append(f"Row {row_num}: Could not parse '{row[x_col]}', '{row[y_col]}'")

            if errors:
                print(f"\nWarnings ({len(errors)} rows skipped):")
                for e in errors[:5]:
                    print(f"  {e}")
                if len(errors) > 5:
                    print(f"  ... and {len(errors) - 5} more")

            if not points:
                print("Error: No valid points found in CSV.")
                continue

            print(f"\nSuccessfully loaded {len(points)} points.")
            if len(points) <= 10:
                print(f"  Points: {points}")
            else:
                print(f"  First 5: {points[:5]}")
                print(f"  Last 5:  {points[-5:]}")

            return points

        except FileNotFoundError:
            print(f"Error: File not found: {filepath}")
        except PermissionError:
            print(f"Error: Permission denied: {filepath}")
        except Exception as e:
            print(f"Error reading CSV: {e}")


def display_multi_result(
    originals: list[Point],
    transformed: list[Point],
    description: str
) -> None:
    """Display transformation results for multiple points."""
    print("\n" + "-" * 50)
    print(f"  {description}")
    print("-" * 50)

    if len(originals) <= 10:
        for i, (orig, trans) in enumerate(zip(originals, transformed), 1):
            print(f"  Point {i}: {orig} -> {trans}")
    else:
        print(f"  Showing first 5 and last 5 of {len(originals)} points:")
        for i in range(5):
            print(f"  Point {i + 1}: {originals[i]} -> {transformed[i]}")
        print("  ...")
        for i in range(len(originals) - 5, len(originals)):
            print(f"  Point {i + 1}: {originals[i]} -> {transformed[i]}")

    print("-" * 50)


def export_results_prompt(
    originals: list[Point],
    transformed: list[Point]
) -> None:
    """Optionally export results to CSV."""
    print("\nExport results to CSV?")
    print_menu(["Yes", "No"])
    if get_menu_choice("Select: ", 2) == 2:
        return

    filepath = input("Enter output file path: ").strip()
    if not filepath:
        print("Export cancelled.")
        return

    try:
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["original_x", "original_y", "transformed_x", "transformed_y"])
            for orig, trans in zip(originals, transformed):
                writer.writerow([orig.x, orig.y, trans.x, trans.y])
        print(f"Results exported to: {filepath}")
    except Exception as e:
        print(f"Error exporting: {e}")
