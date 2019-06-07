T = int(input())
for i in range(0,T):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a%b!=0 or b%a!=0:
        print("YES")
    else:
        print("NO")
        
