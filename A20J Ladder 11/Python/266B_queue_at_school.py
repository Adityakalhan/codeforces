from queue import Queue
def formation_after_t(s,n,t) -> str :
    temp = [char for char in s]
    q = Queue()
    for i in range(t) :
        for j in range(n) :
            if temp[j] == 'B' :
                q.put(j)
        
        while not(q.empty()) :
            boy_index = q.get()
            if boy_index < n-1 and temp[boy_index + 1] == 'G' :
                temp[boy_index + 1],temp[boy_index] = temp[boy_index] , temp[boy_index + 1]

    res = ''
    for char in temp :
        res += char
    return res 

n,t = map(int,input().split())
input_sequence = input()
print(formation_after_t(input_sequence , n, t))