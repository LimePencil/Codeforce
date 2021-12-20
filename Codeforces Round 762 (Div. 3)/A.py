# success

import sys

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    q = sys.stdin.readline().rstrip("\n")
    q1 =q[:len(q)//2]
    q2 = q[len(q)//2:]
    if (q1 != q2):
        print("NO")
    else:
        print("YES")