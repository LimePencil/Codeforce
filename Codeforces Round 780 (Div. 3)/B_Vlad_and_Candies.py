import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)
    ans = "YES"
    if len(arr)==1:
        if arr[0]>=2:
            ans = "NO"
    elif arr[0]-arr[1]>=2:
        ans = "NO"
    print(ans)