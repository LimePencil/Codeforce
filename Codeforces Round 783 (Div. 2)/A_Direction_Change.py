import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a,b=list(map(int,input().split()))
    if b<a:
        a,b=b,a  
    if a==1 and b>=3:
        print(-1)
    else:
        if (b-a)%2==0:
            print(a*2-2+(b-a)*2)
        else:
            print(a*2-2+(b-a-1)*2+1)