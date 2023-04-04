def add_commas(n):
    n = str(n)

    if len(n) < 3:
        return n
    
    return add_commas(n[:-3]) + "," + n[-3:]


print(add_commas('15866321'))