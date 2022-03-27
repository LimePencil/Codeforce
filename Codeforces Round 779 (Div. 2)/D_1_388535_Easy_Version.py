import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ans = 0
    l,r= list(map(int,input().split()))
    arr = list(map(int,input().split()))
    arr.sort()
    found = False
    for i in range(r):
        if arr[i]^arr[i+1] == r:
            print(arr[i])
            print([c^arr[i] for c in arr])
            found = True
            break
    if not found:
        print(arr[r])
        print([c^arr[r] for c in arr])
    
