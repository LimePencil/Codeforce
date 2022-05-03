from math import ceil
import sys

input = sys.stdin.readline
n = int(input())
walls = list(map(int,input().split()))
l=[]
for i in range(len(walls)):
      l.append([walls[i],i])
l.sort()

m=float('inf')
if abs(l[0][1]-l[1][1])==2:
    m=min(m,l[0][0]+ceil((l[1][0]-l[0][0])/2))


temp=walls[:]
amount=0
a=ceil(temp[l[0][1]]/2)
amount+=ceil(a)
temp[l[0][1]]==0
if 0<=l[0][1]-1<n:
    temp[l[0][1]-1]-=a
if 0<=l[0][1]+1<n:
    temp[l[0][1]+1]-=a
temp.sort()
amount+=ceil(temp[1]/2)
m=min(m,amount)

temp=walls[:]
amount=0
a=ceil(temp[l[1][1]]/2)
amount+=ceil(a)
temp[l[1][1]]==0
if 0<=l[1][1]-1<n:
    temp[l[1][1]-1]-=a
if 0<=l[1][1]+1<n:
    temp[l[1][1]+1]-=a
temp.sort()
amount+=ceil(temp[1]/2)
m=min(m,amount)

for i in range(len(walls)-1):
    m=min(m,ceil((walls[i]+walls[i+1])/3))
print(m)