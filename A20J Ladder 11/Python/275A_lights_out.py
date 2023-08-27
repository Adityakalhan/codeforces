def final_state(lights) :
    state = [[1 for i in range(3)]for j in range(3)]
    drow,dcol = [-1,0,1,0],[0,-1,0,1]

    for i in range(3) :
        for j in range(3) :
            time = lights[i][j]
            for t in range(time) :
                state[i][j] = 1 - state[i][j]
                for k in range(4) :
                    nrow,ncol = drow[k] + i, dcol[k] + j
                    if nrow >= 0 and ncol >= 0 and nrow < 3 and ncol < 3 :
                        state[nrow][ncol] = 1 - state[nrow][ncol]

    return state

def get_input() :
    lights = []
    for i in range(3) :
        x,y,z = map(int,input().split())
        lights.append([x,y,z])
    return lights

def print_output(op) :
    for i in range(3) :
        for j in range(3) :
            print(op[i][j],end = '')
        print()


print_output(final_state(get_input()))