import sys
import math

key = input().lower().strip()
n = int(input())

key_length = len(key)

for _ in range(n):
    _str = input().lower().strip()
    if len(_str) != key_length:
        print ("fail")
        continue

    matched_chars = sum(1 for i in range(key_length) if key[i] == _str[i])
    
    accuracy = (matched_chars / key_length) * 100
    if accuracy >= 90:
        print("pass")
    else:
        print("fail")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


