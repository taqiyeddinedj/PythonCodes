def count(string):
    get_count = 0
    for i in string:
        if i == "-":
            get_count += 1
    return get_count +1

print(count("taq-iy-edd-ine"))