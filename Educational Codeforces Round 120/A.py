# pass
import sys

n = int(sys.stdin.readline().rstrip("\n"))
for _ in range(n):
    sticks = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    s = sum(sticks)

    if(s%2 == 1):
        print("NO")
    else:
        found = False
        for k,a in enumerate(sticks):
            if s == 2* a:
                found = True
                break
            elif (k ==0 and sticks[1] == sticks[2]) or (k ==1 and sticks[2] == sticks[0]) or (k ==2 and sticks[1] == sticks[0]):
                found = True
                break
        print("YES" if found else "NO")
