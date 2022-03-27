import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ans = 0
    n= int(input())
    s = input().strip("\n")
    for i in range(n-1):
        if i ==n-2 and s[i]=="0" and s[i+1]=="1":
            pass
        elif i==n-3 and s[i]=="0" and s[i+1]=="1" and s[i+2]=="1":
            pass
        elif s[i]=="0":
            if i+1<n and s[i+1] =="1":
                if i+2<n and s[i+2]=="1":
                    pass
                else:
                    ans+=1
            else:
                ans+=2
    print(ans)