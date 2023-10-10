def add_dots(string):
    s = '.'.join(string)
    return s

def remove_dots(s):
    result = s.replace('.', '')
    return result

print(add_dots('taqiyeddine'))

# Other solution

def addd_dots(string):
    out = ""
    for letter in string:
        out += letter + "."
    return out[:-1]
print(addd_dots('taqiyeddine'))

def removee_dots(string):
    out = ""
    for letter in string:
        if letter  != ".":
            out += letter
    return out
print(removee_dots("t.a.q.i.y.e.d.d.i.n.e"))