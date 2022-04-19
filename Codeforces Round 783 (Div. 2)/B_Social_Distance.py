import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    seats=0
    s=[0]
    for i in range(1,n):
        seats+=1+max(arr[i-1],arr[i])
        s.append(seats)
    seats+=1+max(arr[n-1],arr[0])
    s.append(seats)
    print("YES" if seats<=m else "NO")