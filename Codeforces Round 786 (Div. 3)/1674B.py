import sys

input = sys.stdin.readline
for _ in range(int(input())):
    s=input().rstrip()
    ans=0
    ans+=25*(ord(s[0])-97)
    ans+=(ord(s[1])-97+1 if ord(s[1])<ord(s[0]) else ord(s[1])-97)
    print(ans)