# import sys

# input = sys.stdin.readline

# for _ in range(int(input())):
#     n=int(input())
#     want = ["W"]+list(input().rstrip("\n"))
#     now=["W"]*(n+2)
#     can=True
#     for i in range(1,n+1):
#         if now[i]==want[i]:
#             continue
#         else:
#             if want[i]=="W":
#                 can=False
#                 break
#             elif want[i]=="B":
#                 now[i]="B"
#                 if now[i-1]!="R":
#                     now[i+1]="R"
#             else:
#                 now[i]="R"
#                 if now[i-1]!="B":
#                     now[i+1]="B"
#     if now[n+1]!="W":
#         can=False
#     print("YES" if can else "NO")

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    want = list(input().rstrip("\n"))
    now=[]
    can=True
    for i in want:
        if len(now)!=0:
            if now[-1]!=i:
                now.append(i)
        else:
            now.append(i)
    b=False
    r=False
    only_white=True
    for i in range(len(now)):
        if now[i]=="W":
            if ((not b) or (not r)) and not only_white:
                can=False
                break
            b=False
            r=False
        elif now[i]=="R":
            r=True
            only_white=False
        else:
            only_white=False
            b=True
    if ((not b) or (not r)) and now[-1]!="W" and not only_white:
        can=False
    print("YES" if can else "NO")
