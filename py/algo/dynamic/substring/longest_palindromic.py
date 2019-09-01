
def convert(string):
    new = "|"
    for ch in string:
        new += ch+"|"
    return new

def longest_palindrom(string):
    n = len(string)*2 + 1 
    lps = [0 for i in range(n)]
    new = convert(string)
    lps[1] = 1
    center = 1
    right  = 2
    
    max_len    = 0
    max_center = -1

    for i in range(2,n):
        mirror = center - (i - center)
        lps[i] = 0
        dist   = right - i
        if dist > 0:
            lps[i] = min(lps[mirror], dist)
        
        while   (i + lps[i] + 1 < n) and (i - lps[i] - 1 > 0) and \
                (i + lps[i] + 1 % 2 == 0 or  new[(i+lps[i]+1)] == new[i-lps[i]-1]):
            lps[i] += 1

        if lps[i] > max_len:
            max_len    = lps[i]
            max_center = i 

        if i + lps[i] > right:
            center = i
            right  = i + lps[i]

    if max_center % 2 == 1:
        off = (max_len - 1)//2
        length = 2*off+1
    else:
        off = max_len//2
        length = 2*off
    start = (max_center)//2 - off
    print(string[start:start+length])
    return start, length
    
if __name__ == "__main__":
    for i in ("babcbabcbaccba","abacdfgdcaba","abacdfgdcabba","forgeeksskeegfor"):
        longest_palindrom(i)