def final(s1,s2) :
    res = ""
    for i in range(len(s1)) :
        if s1[i] == s2[i] :
            res += '0'
        else :
            res += "1"
    return res




n1 = input()
n2 = input()
print(final(n1,n2))