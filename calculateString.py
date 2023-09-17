import sys
import math

# For a give string which must be a numbner 
# Calculte this: Input=25 , Output=2*5=10

num = input()

res = 1
for n in num:
    res = res * int(n)

print(f"Result is {res}")