T = int(input())
for i in range(0,T):
    N = int(input())
    S = input()
    c = 0
    if N==1:
        if S=='0':
            print(1)
        else:
            print(0)
    else:
        if S[0]=='0' and S[1]=='0':
            c += 1
        if S[N-1]=='0' and S[N-2]=='0':
            c += 1
        for i in range(1,N-1):
            if S[i]=='0':
                if S[i-1]=='0' and S[i+1]=='0':
                    c += 1
        print(c)
