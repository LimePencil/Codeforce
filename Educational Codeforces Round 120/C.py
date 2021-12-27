# TLE
import sys
import math

t = int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    arr =list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    arr.sort()
    s = sum(arr)
    count = 0
    ans = []
    found = False
    i=0
    if s >k:
        while not found:
            if arr[0]*n <=k:
                found = True
                decreasing = False
                if s>k:
                    while not decreasing:
                        ans.append(count)
                        temp = s
                        for a in range(n-1,0,-1):
                            if arr[0] != arr[a]:
                                ans[i] +=1
                                s-= arr[a]-arr[0]
                                if s <=k:
                                    break
                        if i != 0 and ans[i] > ans[i-1]:
                            break
                        i+=1
                        arr[0]-= 1
                        count+=1
                        s= temp-1
                else:
                    ans.append(count)     
            else:
                m = math.ceil(k/(n*arr[0]))
                arr[0] -=m
                s -=m
                count+=m
    else:
        ans.append(count)
    print((str(ans[-1]) if ans[-1]< ans[-2] else str(ans[-2])) if len(ans) >1 else str(ans[0]))
    