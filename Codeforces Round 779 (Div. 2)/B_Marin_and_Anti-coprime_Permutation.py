import sys
input = sys.stdin.readline
t = int(input())
MOD= 998244353
for _ in range(t):
    ans = 1
    n = int(input())
    if n %2 ==1:
        print("0")
    else:
        for i in range(2,n//2+1):
            ans*=i
            ans%=MOD
        print(pow(ans,2,MOD))