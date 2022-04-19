import sys

input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    pre_sum=[[0]*n for _ in range(n)]
    for i in range(n):
        pre_sum[i][i]=arr[i]
    for i in range(0,n):
        for j in range(i,n):
            pre_sum[i][j]=arr[j]+pre_sum[i][j-1]
    idx=0
    layer=0
    ans=0



