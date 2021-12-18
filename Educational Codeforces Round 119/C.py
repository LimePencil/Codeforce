import sys

a = int(sys.stdin.readline().rstrip("\n"))


    
for _ in range(a):
    n, k, x = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    x = x-1
    s = sys.stdin.readline().rstrip("\n")
    l = []
    where = []
    for index,i in enumerate(s):
        if index ==0:
            if i =="*":
                l.append(k+1)
                where.append(len(l)-1)
            else:
                l.append(0)
        elif i == "*"  and l[-1] == 0:
            l.append(k+1)
            where.append(len(l)-1)
        elif i == "*" and l[-1] != 0:
            l[-1] += k
        else:
            l.append(0)
    ans = []
    for z in reversed(where):
        ans.append("b"*(x%l[z]))
        x = x//(l[z])
    real_ans = "a".join(reversed(ans))
    if(l[0] == 0):
        real_ans = "a" +real_ans
    if(l[-1] == 0):
        real_ans = real_ans + "a"
    print(real_ans)
            