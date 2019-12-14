T = int(input())
for i in range(0,T):
    A = int(input(),2)
    B = int(input(),2)
    cnt=0
    if B==0:
        print(0)
    B = int(B)
    A = int(A)
    while B != 0:
        U = A ^ B
        V = A & B
        A = U
        B = V * 2
        cnt=cnt+1
        if B ==0:
            print(cnt)
