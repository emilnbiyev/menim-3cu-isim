import random

n = 2  
m = 4  
A = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]


sütun_sayısı = len(A[0]) 
B = []  

for j in range(sütun_sayısı):
    cəm = 0
    for i in range(len(A)):
        cəm += A[i][j]
    B.append([cəm])


print("A matrisi:")
for sira in A:
    print(sira)

print("\nB massivi:")
for sira in B:
    print(sira)
