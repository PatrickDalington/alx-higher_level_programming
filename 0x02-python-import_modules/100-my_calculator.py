#!/usr/bin/python3

from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    import sys

    arg = len(sys.argv) - 1

    if arg < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if arg >= 3 and sys.argv[2] in ("*", "+", "-", "/"):
        ans = 0
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == '+':
            ans = add(a, b)
        elif sys.argv[2] == '-':
            ans = sub(a, b)
        elif sys.argv[2] == '*':
            ans = mul(a, b)
        elif sys.argv[2] == '/':
            ans = div(a, b)
        print("{} {} {} = {}".format(a, sys.argv[2], b, ans))
    elif arg >= 3 and sys.argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
