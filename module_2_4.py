numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes =[]
is_prime = True
for i in range(2, len(numbers)+1): #исключаем из процесса единицу
    t = 0 #считаем количество делителей
    for j in range(1, i+1):
        if (i) % j == 0:
           t += 1
        if t > 2:
            break
    if t == 2: #признак простого числа (всего два делителя)
        is_prime == 1
        primes.append(i)
    else:
        is_prime == 0
        not_primes.append(i)
print(primes)
print(not_primes)
