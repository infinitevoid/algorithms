

def longeset_common_substring(a, b):
    row = [0 for j in range(len(b)+1)]
    table = [row[:] for i in range(len(a)+1)]
    result = 0
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if j == 0 or i == 0:
                table[i][j] = 0
            elif a[i-1] == b[j-1]:
                value = table[i][j] = table[i-1][j-1]+1
                result = max(result, value)
    return result


if __name__ == "__main__":
    a = "www.wikipedia.de"
    b = "www.google.de"
    print(longeset_common_substring(a,b))