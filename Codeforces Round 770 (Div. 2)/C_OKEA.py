import sys

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    ans = 0
    n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    if n== 1:
        if k ==1:
            print("YES")
            print("1")
        else:
            print("NO")
    elif n%2==1:
        if k==1:
            print("YES")
            for i in range(1,n+1):
                print(i)
        else:
            print("NO")
    else:
        print("YES")
        for i in range(n//2):
            print(" ".join(map(str,(range(1+i*k*2,(i+1)*k*2+1,2)))))
            print(" ".join(map(str,(range(2+i*k*2,(i+1)*k*2+1,2)))))