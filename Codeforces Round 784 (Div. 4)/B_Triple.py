import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))
    a=Counter(arr)
    found=False
    for c in a.keys():
        if a[c]>=3:
            print(c)
            found=True
            break
    if found==False:
        print("-1")