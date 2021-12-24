import sys
import time


n = int(sys.stdin.readline().rstrip("\n"))
start = time.time()
ans = []
for _ in range(n):
    l,r = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    l -=1
    longest = len(bin(r))-2
    bits_r = [0]*longest
    longest_l = len(bin(l))-2
    for i in range(longest):
        a =  (r+1)//(2**(longest-i))*2**(longest-i-1)
        c = (r+1)%(2**(longest-i))-2**(longest-i-1)
        b= max(0,c)
        bits_r[i] = a + b
    for i in range(longest_l):
        a =  (l+1)//(2**(longest_l-i))*2**(longest_l-i-1)
        c = (l+1)%(2**(longest_l-i))-2**(longest_l-i-1)
        b= max(0,c)
        bits_r[i+(longest-longest_l)] -= a + b

    
    ans.append(str((r-l) - max(bits_r)))
print("\n".join(ans))
    