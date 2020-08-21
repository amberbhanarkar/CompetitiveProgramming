T = int(input())
the = [[0 for i in range(0,4)]for j in range(0,4)]
9pm = []
6pm = []
3pm = []
12pm = []
def twelve(cost):
    su = 0
    for i in range(0,4):
        su += the[0][i]
    return su

def three(cost):
    su = 0
    for i in range(0,4):
        su += the[1][i]
    return su

def six(cost):
    su = 0
    for i in range(0,4):
        su += the[2][i]
    return su

def nine(cost):
    su = 0
    for i in range(0,4):
        su += the[3][i]
    return su

for i in range(0,T):
    N = int(input())
    for j in range(0,N):
        m, t = input()
        t = int(t)
        if m=='A' and t==12:
            the[0][0] += 1
        elif m=='A' and t==3:
            the[0][1] += 1
        elif m=='A' and t==6:
            the[0][2] += 1
        elif m=='A' and t==9:
            the[0][3] += 1
        elif m=='B' and t==12:
            the[1][0] += 1
        elif m=='B' and t==3:
            the[1][1] += 1
        elif m=='B' and t==6:
            the[1][2] += 1
        elif m=='B' and t==9:
            the[1][3] += 1
        elif m=='C' and t==12:
            the[2][0] += 1
        elif m=='C' and t==3:
            the[2][1] += 1
        elif m=='C' and t==6:
            the[2][2] += 1
        elif m=='C' and t==9:
            the[2][3] += 1
        elif m=='D' and t==12:
            the[3][0] += 1
        elif m=='D' and t==3:
            the[3][1] += 1
        elif m=='D' and t==6:
            the[3][2] += 1
        elif m=='A' and t==9:
            the[3][3] += 1
        cost = 100
        k=0
        x=0
        y=0
        w=0
        for k in range(0,4):
            a = twelve(cost)
            12pm.append(a)
            cost -= 25
        for k in range(0,4):
            a = three(cost)
            3pm.append(a)
            cost -= 25
        for k in range(0,4):
            a = six(cost)
            6pm.append(a)
            cost -= 25
        for k in range(0,4):
            a = nine(cost)
            9pm.append(a)
            cost -= 25
        su = 0
        su += 9pm[0]+
                        
        
    
