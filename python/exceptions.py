# Need to import the system error

import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)


# Handling Exception

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # exit the program with status code of 1 (something went wrong)
    sys.exit(1)

print(f"{x} / {y} = {result}")