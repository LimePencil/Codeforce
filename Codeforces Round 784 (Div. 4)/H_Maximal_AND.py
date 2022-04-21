import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    ans=0
    num=[0]*31
    for i in range(n):
        s='{:031b}'.format(arr[i])
        for j in range(31):
            if s[j]=="1":
                num[j]+=1
    ans=0
    for i in range(31):
        if n-num[i]<=k:
            k-=n-num[i]
            num[i]=n
            ans|=1<<(30-i)
    print(ans)