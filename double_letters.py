def double_letters(s):
    for i in range(len(s) - 1): # 3
        if s[i] == s[i + 1]: # s[0] => a; a == l
            return True
    return False

print(double_letters('alaxa'))

 # short version provided by site's solution:
 #def double_letters(string):
    #return any([a == b for a, b in zip(string, string[1:])])