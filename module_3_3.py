def print_params(a=1, b='строка', c=True):
    print(a, b, c)
values_list = [True, tuple, 14]
values_list_2 = [[7.5, 8], False]
values_dict = {'a': 'One', 'b': 'Two', 'c': 'Three'}

print_params(*values_list)
print_params(**values_dict)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list_2, 42)

