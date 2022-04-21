import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))
    odd=True
    can=True
    for i in range(0,len(arr),2):
        if i==0:
            if arr[i]%2==0:
                odd=False
        else:
            if odd and arr[i]%2==0:
                can=False
                break
            elif not odd and arr[i]%2==1:
                can=False
                break
    odd=True
    can2=True
    for i in range(1,len(arr),2):
        if i==1:
            if arr[i]%2==0:
                odd=False
        else:
            if odd and arr[i]%2==0:
                can2=False
                break
            elif not odd and arr[i]%2==1:
                can2=False
                break
    if can and can2:
        print("YES")
    else:
        print("NO")