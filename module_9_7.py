def is_prime(func):
    def wrapper(*args: int):
        result = func(*args)
        if result == 0 or result == 1:
            print(f'Число {result} не является ни простым, ни составным')
        else:
            for i in range(2, result // 2 + 1):
                if result % i == 0:
                    print("Составное")
                    return result
            print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c: int):
    result = a + b + c
    return result


result = sum_three(0, 0, 1)
print(result)
