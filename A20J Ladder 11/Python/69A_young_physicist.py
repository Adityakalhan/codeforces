def vector_sum(vector) :
    x_component,y_component,z_component = 0,0,0
    for x,y,z in vector :
        x_component += x
        y_component += y
        z_component += z
    if z_component == 0 and y_component == 0 and x_component == 0 :
        print("YES")
    else :
        print("NO")
n = int(input())
vectors = []
for i in range(n) :
    component = tuple(map(int,input().split()))
    vectors.append(component)
vector_sum(vectors)