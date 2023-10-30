def flatten(lists):
    result = []
    for sublist in lists:
        for i in sublist:   
            result.append(i)
    return result

lists = [[1, 2], [3, 4]]

print(flatten(lists))