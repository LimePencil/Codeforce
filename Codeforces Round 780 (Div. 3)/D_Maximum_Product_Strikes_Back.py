import sys
import random

def find_ans(s,e):
    if s>e:
        return -1,0,0
    mul = 1
    for i in range(s,e+1):
        mul*=arr[i]
        if arr[i]==0:
            s1,a1,b1 = find_ans(s,i-1)
            s2,a2,b2 = find_ans(i+1,e)
            if s1>s2:
                return s1,a1,b1+e-i+1
            else:
                return s2,a2+i-s+1,b2
    if mul>0:
        return mul,0,0
    else:
        idx1 = s
        new_mul1 = 1
        while idx1<=e:
            new_mul1 *= arr[idx1]
            if arr[idx1]<0:
                break
            idx1+=1
        idx2 = e
        new_mul2 = 1
        while idx2>=s:
            new_mul2 *= arr[idx2]
            if arr[idx2]<0:
                break
            idx2-=1
        if new_mul1<new_mul2:
            return mul//new_mul2,0,e-idx2+1
        else:
            return mul//new_mul1,idx1-s+1,0

input = sys.stdin.readline
sys.setrecursionlimit(3*10**5)
t = int(input())
for _ in range(t):
    n=int(input())
    arr = [random.randint(-2,2) for _ in range(n)]
    a = 0
    b = 0
    c = 0
    while len(arr)!=0 and arr[0] == 0:
        a+=1
        arr.pop(0)
    while len(arr)!=0 and arr[-1] == 0:
        b+=1
        arr.pop()
    _,x,y=find_ans(a,n-1-b)

    print(x+a,y+b)