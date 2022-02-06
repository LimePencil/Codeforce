import sys
import math

def is_palindrom(s):
    length = len(s) 
    for i in range(math.floor(length / 2)):
        if s[i] != s[length - i - 1]:
            return False
    return True

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n,k = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
    a = sys.stdin.readline().rstrip("\n")
    if k == 0:
        print("1")
    else:
        if is_palindrom(a):
            print("1")
        else:
            print("2")
