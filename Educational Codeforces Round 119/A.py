# pass

import sys

n = int(sys.stdin.readline().rstrip("\n"))

for _ in range(n):
    q = sys.stdin.readline().rstrip("\n")
    predicted = [0]
    count = 0
    for i,e in enumerate(q):
        if e == "N":
            count += 1
    if (count == 1):
        print("NO")
    else:
        print("YES")
        
# import sys

# n = int(sys.stdin.readline().rstrip("\n"))

# for _ in range(n):
#     q = sys.stdin.readline().rstrip("\n")
#     predicted = [0]
#     for i,e in enumerate(q):
#         if(e == "E"):
#             predicted.append(predicted[i-1])
#         elif(e == "N"):
#             predicted.append(predicted[i-1]+1)
#     if ((q[0] == "E" and q[0] != q[-1]) or (q[0] == "F" and q[0] == q[-1])):
#         print("NO")
#     else:
#         print("YES")
        
