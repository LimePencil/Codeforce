# pass
import sys

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip("\n"))
    ratings = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    likes = sys.stdin.readline().rstrip("\n")
    new_1 = []
    new_0 = []
    for k,i in enumerate(likes):
        if i =="1":
            new_1.append((ratings[k],k))
        else:
            new_0.append((ratings[k],k))
    new_1_s = sorted(new_1,key=lambda x: x[0],reverse=True)
    new_0_s = sorted(new_0,key=lambda x: x[0],reverse=True)
    for k,i in new_1_s:
        ratings[i] = n
        n-=1
    for k,i in new_0_s:
        ratings[i] = n
        n-=1
    print(*ratings)