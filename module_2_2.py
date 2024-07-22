first = (int(input('Введите любое целое число: ')))
second = (int(input('Введите любое целое число: ')))
third = (int(input('Введите любое целое число: ')))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
# Или так
#elif not (first == second or first == third or second == third):
#    print(0)
else:
    print(0)