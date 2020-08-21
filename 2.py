K = 20
aa = 'abcdefghijklmnopqrstuvwxyz'
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
P = input()
C = []
for i in range(0,len(P)):
    d = ((P[i]+K))%26
    C.append(d)
print(C)
E = []
for i in range(0,len(C)):
    d = (C[i]-K)%26
    E.append(d)
print(E)
for i in range(0,len(E)):
    print((a[E[i]]), end=" ")