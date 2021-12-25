# pass

import sys

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    b_num = int(sys.stdin.readline().rstrip("\n"))
    buildings = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    total = sum(buildings)
    if(total % b_num == 0):
        print("0")
    else:
        print("1")
    