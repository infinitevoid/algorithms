

def edit_distance(a, b):
    n, m = len(a), len(b)
    row   = [0 for i in range(n)]
    table = [row[:] for j in range(m)]
    for i in range(n):
        for j in range(m):
            if i == 0:
                table[j][i] = j
            elif j == 0:
                table[j][i] = i
            elif a[i] == b[j]:
                table[j][i] = table[j-1][i-1]
            else:
                table[j][i] = 1+min(table[j][i-1],
                                    table[j-1][i],
                                    table[j-1][i-1])
    return table[m-1][n-1]


def edit_distance_rec(a, b, i: int, j: int):
    if i == 0:
        return j
    elif j == 0:
        return i
    elif a[i-1] == b[j-1]:
        return edit_distance_rec(a, b, i - 1, j - 1)
    return 1 +  min(edit_distance_rec(a, b, i - 1, j),
                    edit_distance_rec(a, b, i, j - 1),
                    edit_distance_rec(a, b, i - 1, j - 1))

"""
###Test###
if __name__ == "__main__":
    a = "sunday"
    b = "saturday"
    print(edit_distance(a,b))
    print(edit_distance_rec(a,b,len(a),len(b)))
"""