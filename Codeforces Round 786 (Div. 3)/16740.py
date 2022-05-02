from math import log
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if (not (b/a).is_integer()) or a>b:
        print(0,0)
        continue
    if b==a:
        print(1,1)
        continue
    for i in range(2,100):
        x=log(b//a,i)
        if x.is_integer():
            if x==0:
                x=1
            print(int(x),i)
            break
    else:
        print(0,0)