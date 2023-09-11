import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
m, n = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
def find_divisors(num):
    # i want to find all divisors for both numbers then compare
    divisors = set() # empty set for unique divisors 
    for i in range(1, num+1):
        if num % i == 0:
            divisors.add(i)
    return divisors

divisors_m = find_divisors(m)
divisors_n = find_divisors(n)
print("The number of exclusive divisors are: ")
j=0
k=0
for i in divisors_m:
    if n % i != 0:
        j+=1

for i in divisors_n:
    if m % i != 0:
        k+=1

divisors = j+k
print(divisors)


#print("Starting the program...", file=sys.stderr)
