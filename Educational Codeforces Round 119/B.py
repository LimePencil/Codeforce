import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    w, h = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    x1 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    x2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    y1 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    y2 = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    ans = 0
    corner_points = [(x1[1],0), (x1[-1],0), (x2[1], h), (x2[-1],h), (0,y1[1]), (0,y1[-1]),(w,y2[1]),(w,y2[-1])]
    for i in permutations(range(4),2):
        p1 = corner_points[i[0]*2]
        p2 = corner_points[i[0]*2+1]
        p3 = corner_points[i[1]*2]
        area = abs((p1[0]*p2[1]+ p2[0]*p3[1]+p3[0]*p1[1]-p2[0]*p1[1]-p3[0]*p2[1]-p1[0]*p3[1]))
        ans = max(ans, area)
    print(ans)
