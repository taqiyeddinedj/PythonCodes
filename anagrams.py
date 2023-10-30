def is_anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
print(is_anagram("hrba", "arhab"))
