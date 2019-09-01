

def int_pow(n: int, e: int) -> int:
    if e % 2 == 0:
        temp = int_pow(n, e // 2)
        return temp*temp
    else:
        temp = int_pow(n, e // 2)
        return n*temp*temp