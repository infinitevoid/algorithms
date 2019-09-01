from typing import List, Tuple
from math import atan2


def CCW(a, b, c) -> bool:
    #slope(a,b) = (b[1]-b[0])/(b[0] - a[0]) < (b[1]-c[1])/(b[0]-c[0]) = slope(b,c)
    return (b[1] - b[0]) * (b[0] - c[0]) < (b[1] - c[1]) * (b[0] - a[0]) 

def graham_scan(points: List[Tuple[float, float]]):
    left = min(points)
    angles = []
    for p in points:
        if p != left:
            #atan2(delta y, delta x)
            angle = atan2(p[1]- left[1], p[0] - left[0])
            angles.append((angle, p))
    # sort by first elements
    angles.sort(key = lambda x: x[0])
    
    stack = [left, angles[0][1], angles[1][1]]
    for angle, point in angles[3:]:
        while len(stack) > 1 and CCW(stack[-2], stack[-1], point):
            stack.pop()
        stack.append(point)
    return stack

if __name__ == "__main__":
    points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = graham_scan(points)
    print(hull)