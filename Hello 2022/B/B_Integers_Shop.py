# unable to solve

import sys

t= int(sys.stdin.readline().rstrip("\n"))
for _ in range(t):
    n = int(sys.stdin.readline().rstrip("\n"))
    stuff = []
    largest = []
    smallest = []
    for i in range(n):
        money = 0
        a = list(map(int,sys.stdin.readline().rstrip("\n").split(" ")))
        same = False
        if i == 0:
            largest = a
            smallest = a
            same = True
        else:
            if (largest[0] == a[0] and largest[1] == a[1] and largest[2] > a[2]) and (smallest[0] == a[0] and smallest[1] == a[1] and smallest[2] > a[2]):
                largest = a
                smallest = a
            elif (largest == a and largest[2] > a[2]):
                largest = a
            elif ((smallest == a and smallest[2] > a[2])):
                smallest = a
            elif (a[0] == smallest[0] and a[1]>largest[1]) or (a[0]<smallest[0] and a[2]<largest[2]):
                largest = a
                smallest = a
                same = True
            else:
                if a[0]<smallest[0]:
                    smallest = a
                elif a[0] == smallest[0] and a[2]<smallest[2] and largest != smallest:
                    smallest = a
                            
                if a[1]>largest[1]:
                    largest = a
                elif a[1] == largest[1] and a[2]<largest[2] and largest != smallest:
                    largest = a

            if largest == smallest:
                same = True
        print(largest[2] if same else largest[2]+smallest[2])
                
