import sys

def update(idx, val):
    while idx <= len(s)+1:
        tree[idx]+= val
        idx+= (idx&-idx)

def query(idx):
    ans =0
    while idx>0:
        ans+= tree[idx]
        idx-=(idx&-idx)
    return ans


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = list(input().rstrip("\n"))
    count=[[] for _ in range(26)]
    tree = [0]*(len(s)+1)
    delete = [0]*len(s)
    for j in range(len(s)):
        count[ord(s[j])-97].append(j)
    idx = [0]*26
    k=0
    while k < len(s):
        if delete[k] == 1:
            k+=1
            continue
        now = ord(s[k])-97
        if k+1<len(s):
            next = ord(s[k+1])-97
            if now == next:

        else:
            update(k+1,1)
            delete[k]= 1
        


    print()
