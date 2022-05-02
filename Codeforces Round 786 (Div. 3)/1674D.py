import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    a = list(map(int,input().split()))
    c=sorted(a)
    for i in range(n%2,len(a),2):
        if a[i]>a[i+1]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    if a==c:
        print("YES")
    else:
        print("NO")