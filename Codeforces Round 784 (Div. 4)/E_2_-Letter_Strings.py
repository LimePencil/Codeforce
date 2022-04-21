import sys
from collections import defaultdict

input = sys.stdin.readline

for _ in range(int(input())):
    count=0
    di=defaultdict(int)
    for _ in range(int(input())):
        s=input().rstrip("\n") 
        di[s]+=1 
    d=[]
    num=[]
    for i in di.keys():
        d.append(i)
        num.append(di[i])
    for i in range(len(d)):
        for j in range(i+1,len(d)):
            if d[i][0]==d[j][0] and d[i][1]!=d[j][1]:
                count+=num[i]*num[j]
            elif d[i][0]!=d[j][0] and d[i][1]==d[j][1]:
                count+=num[i]*num[j]

    print(count)