"""A tiny real-number equation solver used to learn testing and CI."""

import argparse
import math


def solve_linear(a: float, b: float) -> float:
    """Return the solution of ax + b = 0."""
    if a == 0:
        raise ValueError("a must be nonzero for a linear equation")
    return -b / a


def solve_quadratic(a: float, b: float, c: float) -> tuple[float, ...]:
    """Return the distinct real roots of ax² + bx + c = 0, sorted."""
    if a == 0:
        raise ValueError("a must be nonzero for a quadratic equation")

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return ()
    if discriminant == 0:
        return (-b / (2 * a),)

    root = math.sqrt(discriminant)
    return tuple(sorted(((-b - root) / (2 * a), (-b + root) / (2 * a))))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Solve a linear or quadratic equation")
    subparsers = parser.add_subparsers(dest="kind", required=True)
    linear = subparsers.add_parser("linear", help="solve ax + b = 0")
    linear.add_argument("a", type=float)
    linear.add_argument("b", type=float)
    quadratic = subparsers.add_parser("quadratic", help="solve ax² + bx + c = 0")
    quadratic.add_argument("a", type=float)
    quadratic.add_argument("b", type=float)
    quadratic.add_argument("c", type=float)
    args = parser.parse_args(argv)

    try:
        roots = (solve_linear(args.a, args.b),) if args.kind == "linear" else solve_quadratic(args.a, args.b, args.c)
    except ValueError as error:
        parser.error(str(error))

    if not roots:
        print("No real solutions")
    else:
        for root in roots:
            print(f"x = {root:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
