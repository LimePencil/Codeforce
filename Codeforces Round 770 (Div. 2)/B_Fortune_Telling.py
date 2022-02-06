# import sys

# def operation(num,nth):
#     global ans
#     if nth == n:
#         ans.append(num)
#         return
#     operation(num+a[nth],nth+1)
#     operation(num^a[nth],nth+1)
# sys.setrecursionlimit(10**5)
# t= int(sys.stdin.readline().rstrip("\n"))
# for _ in range(t):
#     ans = []
#     n,x,y = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
#     a = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
#     s = [0]*(n)
#     s[0] = a[0]
#     for i in range(1,n):
#         s[i] = a[i]+s[i-1]
#     operation(x,0)
#     print(ans)
#     ans = []
#     operation(x+3,0)
#     print(ans)

import sys

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    ans = []
    n,x,y = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    a = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    s = sum(a)
    print("Alice" if (x+s)%2==y%2 else "Bob")

# import sys

# def operation(num,nth):
#     global ans
#     if nth == n:
#         if num == y:
#             ans = num
#         return
#     operation(num+a[nth],nth+1)
#     operation(num^a[nth],nth+1)
# sys.setrecursionlimit(10**5)
# t= int(sys.stdin.readline().rstrip("\n"))
# for _ in range(t):
#     ans = -1
#     n,x,y = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
#     a = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
#     operation(x,0)
#     print("Alice" if ans !=-1 else "Bob")