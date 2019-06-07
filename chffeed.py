T = int(input())
for i in range(0,T):
    S = str(input())
    J = "010"
    H = "101"
    if S.find(J) is not -1:
        print("Good")
    elif S.find(H) is not -1:
        print("Good")
    else:
        print("Bad")
    

