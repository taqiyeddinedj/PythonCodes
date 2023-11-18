def largest_difference(list):
    maximum = max(list)
    minimum  = min(list)
    dif = maximum - minimum
    return dif

print(largest_difference([6,2,1]))