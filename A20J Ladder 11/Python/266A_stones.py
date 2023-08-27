def num_changes(s) :
    prev = s[0]
    cnt = 0
    for i in range(1,len(s)) :
        if prev == s[i] :
            cnt += 1
        else :
            prev = s[i]
    return cnt
n = int(input())
word = input()
print(num_changes(word))