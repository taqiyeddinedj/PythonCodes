import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
temperatures = [] # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temperatures.append(t)

def find_closest(lst):
    # If no temperatures are provided
    if not lst:
        print(0)
        return
    closest = float('inf')  # Initialize with a very large value
    for temp in lst:
        if abs(temp) < abs(closest) or (abs(temp) == abs(closest) and temp > 0): # seconde condition to handle equal values to zero ex: +2 and -2)
            closest = temp     
    print(closest)

find_closest(temperatures)