def return_number(s,n) -> str :
    i = 0
    d = {
        '.' : '0',
        '-.' : '1',
        '--' : '2'
    }
    res = ''
    while i < n :
        if s[i] == '.' :
            res += d[s[i]]
            i += 1
        else :
            seq = s[i] + s[i + 1]
            res += d[seq]
            i += 2
    return res




ternary_notation = input()
print(return_number(ternary_notation,len(ternary_notation)))