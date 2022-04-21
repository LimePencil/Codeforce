import sys

input = sys.stdin.readline
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    arr=[list(input().rstrip("\n")) for _ in range(x)]
    for i in range(y):
        last_obstacle=x
        l=[row[i] for row in arr]
        for j in range(x-1,-1,-1):
            if l[j]=="o":
                last_obstacle=j
            elif l[j]=="*":
                arr[j][i]="."
                arr[last_obstacle-1][i]="*"
                last_obstacle-=1
    for i in range(x):
        print(*arr[i],sep="")
    print()