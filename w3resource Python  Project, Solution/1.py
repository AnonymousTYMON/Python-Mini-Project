# Create a Python project to get the value of Pi to n number of decimal places.
# Note: Input a number and the program will generate PI to the 'nth digit

import math
n = int(input("Enter the number of decimals to calculate to:  "))
Pi = math.pi
Pi = round(Pi, n)
print(Pi)
