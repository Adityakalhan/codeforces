def get_perm(n) :
    try : 
        temp = [i + 1 for i in range(n)]
        for i in range(0,n,2) :
            temp[i],temp[i + 1] = temp[i + 1],temp[i]
        for ele in temp :
            print(ele,end= ' ')
    except Exception as e :
        print(-1)
        return
    
n = int(input())
get_perm(n)