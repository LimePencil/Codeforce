import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    arr = list(map(int,input().split()))
    start=-1
    end=n
    ate1=0
    ate2=0
    same=0
    while not (start==end-1):
        if ate1>=ate2:
            end-=1
            ate2+=arr[end]     
        else:
            start+=1
            ate1+=arr[start]
        if ate1==ate2:
            same=start+n-end+1
    print(same)