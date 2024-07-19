immutable_var = (1, 2, True, 'Орбита', [5, 6, 7], {1, 8})
print(immutable_var)
print(type(immutable_var))
#immutable_var[1] = 'Орбита'
#При попытке изменить значение переменной (переменных) выдается ошибка
    #Traceback (most recent call last):
        # File:\homework5.py", line 4, in <module>
            #   immutable_var[1] = 'Орбита'
                  #TypeError: 'tuple' object does not support item assignment
#Ошибка вызвана тем, что кортеж относится к неизменяемым типам данных,
#хотя внутри может содержать изменяемые типы данных
mutable_list = ['Буря', 'мглою', 'небо', 'кроет', 123]
print(mutable_list)
mutable_list.append((True, 'Орбита'))
print(mutable_list)
mutable_list.remove('небо')
mutable_list.remove('кроет')
print(mutable_list)
mutable_list[2]='закрыла, небо'
print(mutable_list)
#Или
#mutable_list = ['Буря мглою небо кроет', 123]
#print(mutable_list)
#mutable_list.append((True, 'Орбита'))
#print(mutable_list)
#mutable_list[0]='Буря мглою закрыла небо'
#print(mutable_list)