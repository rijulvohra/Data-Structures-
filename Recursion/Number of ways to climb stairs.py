def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    no_ways = staircase(n-1) + staircase(n-2)
    return no_ways

print(staircase(5))
