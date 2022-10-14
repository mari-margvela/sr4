ar = [int(i) for i in input("введите массив: ").split()] 
delta = int(input("введите delta: "))
a = ar[0]

for i in ar:
    a = min(i, a)
b = 0
for i in ar:
    if a + delta == i:
        b += 1    
        
print(b)