T = int(input())
for i in range(0,T):
    N = int(input())
    if 360%N==0:
        print('y ')
    else:
        print('n ')
    if N<=360:
        print('y ')
    else:
        print('n ')
    if N<=26:
        print('y')
    else:
        print('n')
