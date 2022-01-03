# passed
import sys


t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,k =  list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    table = [["." for _ in range(n)] for _ in range(n)]
    if k> (n+1)//2:
        print("-1")
    elif k ==1 and n==1:
        print("R")
    elif k ==0 and n ==1:
        print(".")
    else:
        for i in range(k):
            table[2*i][2*i] = "R"
        for i in range(n):
            print("".join(table[i]))
