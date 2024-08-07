
def calculate_structure_sum(data_structure):
    s = 0
    if isinstance(data_structure, (float, int)):
        s += data_structure
    elif isinstance(data_structure, str):
        s += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for lts in data_structure:
            s += calculate_structure_sum(lts)
    elif isinstance(data_structure, dict):
        for k, v in data_structure.items():
            s += calculate_structure_sum(k) + calculate_structure_sum(v)
    return s


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban',
                 ('Urban2', 35))}])]
print(calculate_structure_sum(data_structure))



