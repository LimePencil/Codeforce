import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

ans=float('inf')
for i in range(n):
    steps=0
    temp=[0]*n
    if i!=0:
        for j in range(i-1,-1,-1):
            s=abs(temp[j+1])//arr[j]+1 
            steps+=s
            temp[j]=-s*arr[j]
    if i!=n-1:
        for j in range(i+1,n):
            s=temp[j-1]//arr[j]+1
            steps+=s
            temp[j]=s*arr[j]
    ans=min(ans,steps)
print(ans)