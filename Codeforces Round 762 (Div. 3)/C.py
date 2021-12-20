# not solve

import sys
from collections import deque


def backtracking(used_a,used_s):
    global a_len, s_len, a, s,b, found,ans
    if found:
        return
    if used_a ==0 and used_s ==0 and not(len(b)==1 and b[0] == "0"):
        found = True
        ans = list(b)
    if used_s >0 and used_a>0:
        
        b_num = int(s[s_len - used_s]) - int(a[a_len - used_a])
        if((s[s_len - used_s] != "0") and (b_num >= 0 and b_num<10)):
            used_a -=1
            used_s -=1
            b.append(str(b_num))
            backtracking(used_a,used_s)
            b.pop()
            used_a +=1
            used_s +=1
        
    if used_s >1 and used_a>0:
        b_num = int(s[s_len - used_s:s_len - used_s+2]) - int(a[a_len - used_a])
        if((s[s_len - used_s:s_len - used_s+2][0] != "0") and (b_num >= 0 and b_num<10)):
            used_a-=1
            used_s -=2
            b.append(str(b_num))
            backtracking(used_a,used_s)
            b.pop()
            used_a +=1
            used_s +=2
    return

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    a,s = sys.stdin.readline().rstrip("\n").split(" ")
    a_len = len(a)
    s_len = len(s)
    a_num = int(a)
    s_num = int(s)
    b= deque()
    ans = -1
    found = False
    backtracking(a_len,s_len)
    if ans != -1:
        ans = "".join(ans)
    print(int(ans))