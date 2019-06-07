T = int(input())
for i in range(0,T):
    N = int(input())
    for i in range(0,63):
        if((0+(i-1)*26)<N<=(2+(i-1)*26)):
            print(2**(i-1),0,0)
        elif((2+(i-1)*26)<N<=(10+(i-1)*26)):
            print(0,2**(i-1),0)
        elif((26*i-16)<N<=26*i):
             print(0,0,2**(i-1))

