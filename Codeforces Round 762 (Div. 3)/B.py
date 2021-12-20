# success

import sys
import math

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    q = int(sys.stdin.readline().rstrip("\n"))
    print(math.floor(q**(1/3)+0.000000000001)+ math.floor(q**(1/2)) - math.floor(q**(1/6)))