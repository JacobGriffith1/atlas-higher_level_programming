#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    last = number % 10

    print(f"{last}", end='')
    return (last)
