from geometric_transforms import (
    Point,
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
from ui import (
    print_header,
    print_menu,
    get_menu_choice,
    get_float,
    get_point,
    get_center_point,
    display_result,
    display_multi_result,
    get_input_mode,
    get_multiple_points,
    get_csv_points,
    export_results_prompt,
)


def apply_translation(points: list[Point]) -> tuple[list[Point], str]:
    """Apply translation to all points."""
    print_header("TRANSLATION")
    print("Enter the translation vector:")
    dx = get_float("  x movement (horizontal): ")
    dy = get_float("  y movement (vertical): ")

    results = [translate(p, dx, dy) for p in points]
    return results, f"Translation by ({dx}, {dy})"


def apply_rotation(points: list[Point]) -> tuple[list[Point], str]:
    """Apply rotation to all points."""
    print_header("ROTATION")

    print("Select rotation angle:")
    print_menu([
        "90 degrees (counterclockwise)",
        "180 degrees",
        "270 degrees (counterclockwise)",
        "Custom angle"
    ])
    angle_choice = get_menu_choice("Select angle: ", 4)

    center = get_center_point()

    if angle_choice == 1:
        results = [rotate_90(p, center) for p in points]
        description = f"Rotation 90° CCW around {center}"
    elif angle_choice == 2:
        results = [rotate_180(p, center) for p in points]
        description = f"Rotation 180° around {center}"
    elif angle_choice == 3:
        results = [rotate_270(p, center) for p in points]
        description = f"Rotation 270° CCW around {center}"
    else:
        degrees = get_float("Enter angle in degrees (positive = counterclockwise): ")
        results = [rotate_custom(p, center, degrees) for p in points]
        description = f"Rotation {degrees}° around {center}"

    return results, description


def apply_reflection(points: list[Point]) -> tuple[list[Point], str]:
    """Apply reflection to all points."""
    print_header("REFLECTION")

    print("Select line of reflection:")
    print_menu([
        "x-axis (y = 0)",
        "y-axis (x = 0)",
        "Horizontal line (y = __)",
        "Vertical line (x = __)",
        "Custom line (y = mx + b)",
    ])
    choice = get_menu_choice("Select line: ", 5)

    if choice == 1:
        results = [reflect_x_axis(p) for p in points]
        description = "Reflection over x-axis (y = 0)"
    elif choice == 2:
        results = [reflect_y_axis(p) for p in points]
        description = "Reflection over y-axis (x = 0)"
    elif choice == 3:
        y_val = get_float("Enter y-value for horizontal line (y = ?): ")
        results = [reflect_horizontal_line(p, y_val) for p in points]
        description = f"Reflection over y = {y_val}"
    elif choice == 4:
        x_val = get_float("Enter x-value for vertical line (x = ?): ")
        results = [reflect_vertical_line(p, x_val) for p in points]
        description = f"Reflection over x = {x_val}"
    else:
        print("\nEnter line equation y = mx + b:")
        m = get_float("  m (slope): ")
        b = get_float("  b (y-intercept): ")
        results = [reflect_custom_line(p, m, b) for p in points]
        description = f"Reflection over y = {m}x + {b}"

    return results, description


def apply_dilation(points: list[Point]) -> tuple[list[Point], str]:
    """Apply dilation to all points."""
    print_header("DILATION")

    center = get_center_point()

    print("\nScale factor:")
    print("  (> 1 enlarges, < 1 shrinks, negative inverts)")
    scale = get_float("Enter scale factor: ")

    results = [dilate(p, center, scale) for p in points]
    return results, f"Dilation by factor {scale} from {center}"


def display_results(originals: list[Point], transformed: list[Point], description: str) -> None:
    """Display results based on number of points."""
    if len(originals) == 1:
        display_result(originals[0], transformed[0], description)
    else:
        display_multi_result(originals, transformed, description)


def run_transformation_loop(points: list[Point]) -> None:
    """
    Run the transformation loop.

    Allows applying multiple transformations in sequence,
    with option to repeat or exit after each.
    """
    current_points = points
    transformation_count = 0

    while True:
        print("\n" + "=" * 40)
        if transformation_count > 0:
            print(f"  Current points (after {transformation_count} transformation(s)):")
            if len(current_points) <= 5:
                for p in current_points:
                    print(f"    {p}")
            else:
                print(f"    {current_points[0]} ... ({len(current_points)} total)")
        print("=" * 40)

        print("\nSelect transformation type:")
        print_menu([
            "Translation",
            "Rotation",
            "Reflection",
            "Dilation",
            "Done (finish transformations)"
        ])
        choice = get_menu_choice("Select transformation: ", 5)

        if choice == 5:
            break

        original_for_display = [p.copy() for p in current_points]

        if choice == 1:
            current_points, description = apply_translation(current_points)
        elif choice == 2:
            current_points, description = apply_rotation(current_points)
        elif choice == 3:
            current_points, description = apply_reflection(current_points)
        else:  # choice == 4
            current_points, description = apply_dilation(current_points)

        display_results(original_for_display, current_points, description)
        transformation_count += 1

        print("\nWhat would you like to do next?")
        print_menu([
            "Apply another transformation to these results",
            "Start over with new points",
            "Exit program"
        ])
        next_choice = get_menu_choice("Select: ", 3)

        if next_choice == 2:
            return  # Return to main to get new points
        elif next_choice == 3:
            if len(current_points) > 1:
                export_results_prompt(points, current_points)
            print("\nGoodbye!")
            exit(0)
        # next_choice == 1 continues the loop

    # Finished transformations
    if transformation_count > 0 and len(current_points) > 1:
        print(f"\nCompleted {transformation_count} transformation(s).")
        export_results_prompt(points, current_points)


def main() -> None:
    """Main program loop."""
    print_header("TRANSFORMATIONS CALCULATOR")
    print("This program applies geometric transformations to points.")

    while True:
        # Get input mode
        input_mode = get_input_mode()

        # Get points based on mode
        if input_mode == 1:
            point = get_point("\nEnter the point to transform:")
            points = [point]
        elif input_mode == 2:
            points = get_multiple_points()
        else:
            points = get_csv_points()

        # Run transformation loop
        run_transformation_loop(points)

        # Ask to continue with new points
        print("\nStart over with new points?")
        print_menu(["Yes", "No"])
        if get_menu_choice("Select: ", 2) == 2:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
