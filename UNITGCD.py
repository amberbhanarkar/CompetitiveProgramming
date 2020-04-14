T = int(input())
for i in range(0,T):
    N = int(input())
    if N==1:
        print(1)
    else:
        print(N//2)
    if N%2==0:
        for j in range(1,N,2):
            print(2, j, j+1)
    else:
        if N==1:
            #print(1)
            print('1 1')
        elif N==3:
            #print(1)
            print('3 1 2 3')
        elif N==5:
            print('3 1 2 3')
            print('2 4 5')
        else:
            print('3 1 2', N)
            for j in range(3,N,2):
                print(2, j, j+1)
            
            
        
            

