from typing import List, Callable

def kmp_search(string: str, pattern: str, report: Callable):
    lps = longest_prefix_suffix(pattern)
    i,j = 0,0
    while i < len(string):
        if pattern[j] == string[i]:
            i += 1
            j += 1
        if j == len(pattern):
            report(i-j)
            j = lps[j-1]
        elif i < len(string) and string[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


def longest_prefix_suffix(pattern: str) -> List[int]:
    lps = [0]
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps.append(length) #lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps.append(0) #lps[i] = 0
                i += 1
    return lps

"""
###Test###
if __name__ == "__main__":
    print(longest_prefix_suffix("aaacaaaa"))
    print(kmp_search("aaaaacaaaacacacacaaaaaca", "aca", print))
"""