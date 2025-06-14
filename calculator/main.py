# main.py

import sys
from pkg.calculator import Calculator
from pkg.render import render


def main():
    calculator = Calculator()
    expression = "3 + 7 * 2"
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        with open("output.txt", "w") as f:
            f.write(to_print)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()