def islucky(num) :
    s = str(num)
    for char in s :
        if char != "4" and char != "7" :
            print("NO")
            return
    print("YES")
    return
def is_nearly_lucky(num) :
    s = str(num)
    cnt = 0 
    for char in s :
        if char == "4" or char =="7" :
            cnt += 1
    islucky(cnt)
num = int(input())
is_nearly_lucky(num)