import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    ans = a+2*b+1
    if a ==0:
        ans = 1
    print(ans)