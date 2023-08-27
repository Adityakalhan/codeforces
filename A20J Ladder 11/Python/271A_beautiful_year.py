def get_next_year(year) :
    for next_year in range(year + 1,9001) :
        s = str(next_year)
        unique = set()
        for char in s :
            if char not in unique :
                unique.add(char)
            else :
                break
        if len(unique) == 4 :
            return next_year
    return 9012

year = int(input())
print(get_next_year(year))