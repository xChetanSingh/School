h = 4

for x in range(0,h):
    for i in range(0,h-x):
        print(" ",end='')
    for j in range(0, 2*x + 1):
        print("*",end="")
    print()

for x in range(h - 2, -1, -1):
    for i in range(0,h-x):
        print(" ",end='')
    for j in range(0,2*x + 1):
        print("*",end="")
    print()









for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
