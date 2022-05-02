import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s=input().rstrip()
    t=input().rstrip()
    if t=="a":
        print(1)
    elif "a" in t:
        print(-1)
    else:
        print(2**len(s))