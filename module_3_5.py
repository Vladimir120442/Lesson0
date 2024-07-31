def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str(number)) > 1:
        result = first * get_multiplied_digits(int(str_number[1:]))
        return result
    return first

result = get_multiplied_digits(40203)
print(result)
