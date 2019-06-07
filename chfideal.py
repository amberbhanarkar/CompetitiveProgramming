import random
X = random.randint(1,3)
print(X)
Y = random.randint(1,3)
while X==Y:
    Y = random.randint(1,3)
print(Y)
Z = random.randint(1,3)
while Y==Z or X==Z:
    Z = random.randint(1,3)
print(Z)

