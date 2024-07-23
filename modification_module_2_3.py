my_list = [42, 1, 0, 3, 99, 0, 0, 1, 5]
in_value = int(0)
while in_value < len(my_list):
    if(my_list[in_value]) > 0:
        print(my_list[in_value])
    in_value = in_value + 1
# Или так
# while in_value + 1 <= len(my_list):
#     if(my_list[in_value]) > 0:
#         print(my_list[in_value])
#     in_value = in_value + 1
