def can_divide(n) :
    if n > 2 and n%2 == 0 :
        return "YES"
    return "NO"


n = int(input())
ans = can_divide(n)
print(ans)