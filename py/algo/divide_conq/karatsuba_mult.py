

def bitlen(n: int):
    i = 0
    while (1 << i) <= n:
        i += 1
    return i

def even_bitlen(n: int):
    fl = bitlen(n)
    if fl % 2 != 0:
        return fl + 1
    return fl

def karatsuba_mult(x: int, y: int):
    #base cases
    if x == 0 or y == 0:
        return 0
    elif x == 1 or y == 1:
        if x == 1 and y == 1: 
            return 1
        elif x == 1: 
            return y
        else: 
            return x
    #karatsuba algorithm
    n = max(even_bitlen(x), even_bitlen(y))
    mid = n//2
    ceil_mid = mid if mid == n-mid else mid+1
    xl = x >> mid
    xr = x - (xl << mid)
    yl = y >> mid
    yr = y - (yl << mid)
    l = karatsuba_mult(xl, yl)
    r = karatsuba_mult(xr, yr)
    m = karatsuba_mult(xl+xr, yl+yr) - l - r
    return (l << n) + (m << ceil_mid) + r
    
"""
###Test###
if __name__ == "__main__":
    import random
    a = random.randint(0,1234)
    b = random.randint(0,1234)
    print(a*b,karatsuba_mult(a,b))
"""
