def get_correct(s) :
    upper,lower = 0,0
    for char in s :
        if 97 <= ord(char) :
            lower += 1
        else :
            upper += 1
    res = ''
    if upper <= lower :
        for char in s :
            res += char.lower()
    else :
        for char in s :
            res += char.upper()
    return res
word = input()
print(get_correct(word))