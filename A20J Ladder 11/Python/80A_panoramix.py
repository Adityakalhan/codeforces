def next_prime(n,m) :
    for num in range(n+1,51) :
        if num%2 != 0 :
            i = 3
            is_prime = True
            while i < num/2 :
                if num%i == 0 :
                    is_prime = False
                    break
                i += 1
            if is_prime :
                return num == m
    return False

n,m = map(int,input().split())
if (next_prime(n,m)) :
    print("YES")
else :
    print("NO")