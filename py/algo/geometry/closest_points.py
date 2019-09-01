from typing import List,Tuple
from math import hypot

def dist(a: Tuple[int,int], b: Tuple[int,int]) -> float:
    return hypot(a[0]-b[0], a[1]-b[1])

def closest_pair(points: List) -> float:
    px = list(sorted(points, key = lambda x: x[0]))
    py = list(sorted(points, key = lambda x: x[1]))
    return closest_pair_rec(px, py, 0, len(points))

def closest_pair_rec(px: List, py: List, left: int, right: int) -> float:
    if right-left == 1:
        return float('inf')
    elif right-left == 2:
        return dist(px[left],px[left+1])
    ind = (left+right)//2
    mid = px[ind]

    pyl, pyr = [], []

    for p in py:
        if p[0] < mid[0]:
            pyl.append(p)
        else:
            pyr.append(p)

    left  = closest_pair_rec(px, pyl, left, ind)
    right = closest_pair_rec(px, pyr, ind, right)

    dis = min(left,right)

    strip = []
    for p in py:
        if abs(p[0]-mid[0]) < dis:
            strip.append(p)
    
    return min(dis, closest_pair_strip(strip,dis))

def closest_pair_strip(strip: List[Tuple[int,int]], min_dis: float) -> float:
    # one can proof that the inner loop runs at most 6 times
    # hint: draw a rect with height min_dis and width 2*min_dis
    # now try to distribute more than 6 points so that every 
    # pair of points a,b satisfies dist(a,b) >= min_dist
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if abs(strip[i][1]-strip[j][1]) < min_dis:
                d = dist(strip[i], strip[j])
                if d < min_dis: min_dis = d
            else:
                break
    return min_dis

"""
###Test###
if __name__ == "__main__":
    arr = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(closest_pair(arr))
"""