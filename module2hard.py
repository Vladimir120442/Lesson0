import random
n = random.randint(3,20)
result = []
j = 1
for i in range(1, n):
    dl = []
    j = i
    for j in range(j, n):
        if n % (i+j) == 0 and i != j:
            dl1 = (f'{i}{j}')
            result.append(dl1)
result = ''.join(result)
print(n, '-', result)
