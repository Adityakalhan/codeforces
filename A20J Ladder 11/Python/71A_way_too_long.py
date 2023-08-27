def abbreviate_string(s) :
    if len(s) <= 10 :
        return s
    
    first = s[0]
    last = s[-1]
    res = first + str(len(s) - 2) + last
    return res

t = int(input())
tc = []
for i in range(t) :
    word = input()
    tc.append(word)
for i in range(t) :
    print(abbreviate_string(tc[i]))
