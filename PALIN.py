T = int(input())
def reverse(a):
    return a[::-1]

for i in range(0,T):
    K = int(input())
    for j in range(K+1,99999999):
        a = str(j)
        b = reverse(a)
        if str(j)==b:
            print(j)
            break
