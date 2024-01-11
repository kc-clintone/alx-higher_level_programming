#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def calc(a, operator, b):
    if op == '+':
        result = add(int(a), int(b))
    elif op == '-':
        result = sub(int(a), int(b))
    elif op == '*':
        result = mul(int(a), int(b))
    elif op == '/':
        result = div(int(a), int(b))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, op, b = sys.argv[1], sys.argv[2], sys.argv[3]
    calculator(a, op, b)

