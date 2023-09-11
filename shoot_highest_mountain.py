import sys

# game loop
while True:
    height = 0
    index_h = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if 0 <= mountain_h <= 9:  # Adjusted condition to include 0 and 9
            if mountain_h > height:
                height = mountain_h
                index_h = i

    # The index of the mountain to fire on.
    print(index_h)
