T = int(input())
for i in range(0,T):
    S, W1, W2, W3 = map(int,input().split())
    if S==1:
        print(W1+W2+W3)
    elif W1==W2==W3==1 and S==2:
        print(2)
    elif W1==W2==W3==1 and S>=3:
        print(1)
    elif W1==W2==W3==2 and (S==2 or S==3):
        print(3)
    elif W1==W2==W3==2 and (S==4 or S==5):
        print(2)
    elif W1==W2==W3==2 and S>=6:
        print(1)
    elif (W1==1 and W2==2 and W3==1) and S==2:
        print(3)
    elif (W1==1 and W2==2 and W3==1) and S==3:
        print(2)
    elif (W1==1 and W2==2 and W3==1) and S>=4:
        print(1)
    elif (W1==2 and W2==1 and W3==2) and S==2:
        print(3)
    elif (W1==2 and W2==1 and W3==2) and (S==3 or S==4):
        print(2)
    elif (W1==2 and W2==1 and W3==2) and S>=5:
        print(1)
    elif (W1==1 and W2==1 and W3==2) and (S==2 or S==3):
        print(2)
    elif (W1==1 and W2==1 and W3==2) and S>=4:
        print(1)
    elif (W1==1 and W2==2 and W3==2) and S==2:
        print(3)
    elif (W1==1 and W2==2 and W3==2) and (S==3 or S==4):
        print(2)
    elif (W1==1 and W2==2 and W3==2) and S>=5:
        print(1)
    elif (W1==2 and W2==1 and W3==1) and (S==2 or S==3):
        print(2)
    elif (W1==2 and W2==1 and W3==1) and S>=4:
        print(1)
    elif (W1==2 and W2==2 and W3==1) and S==2:
        print(3)
    elif (W1==2 and W2==2 and W3==1) and (S==3 or S==4):
        print(2)
    elif (W1==2 and W2==2 and W3==1) and S>=5:
        print(1)
    else:
        break
         
        
        
