x = []

y = int(input("размерность массива: "))
ar = [float(i) for i in input().split()]
imax = 0
for i in range(1, n):
    if (ar[i] >= ar[imax]):
        imax = i
for i in range (imax + 1, n):
    ar[i] = 0
print(ar)

