A=[1,2,3,4,5,6,12]
K=2

for i in range(K):
    O=A.pop()
    A.insert(0,O)
print(A)
