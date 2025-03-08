#!/usr/bin/env python3
# Author ID: pkaur515

def add(number1, number2):
    try:
        # Convert inputs to integers
        num1 = int(number1)
        num2 = int(number2)
        return num1 + num2
    except (ValueError, TypeError):
        return 'error: could not add numbers'


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except Exception:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # works
    print(add('10', 5))                      # works
    print(add('abc', 5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception
