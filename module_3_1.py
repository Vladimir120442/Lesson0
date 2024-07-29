calls = 0
def count_calls(calls1):
    global calls
    calls = calls + 1
    print(calls)

def string_info():
    count_calls(calls)
    string = 'Программирование'
    string = (len(string), string.upper(), string.lower())
    print(string)

def is_contains():
    count_calls(calls)
    string = ('Небо')
    string = string.upper()
    list_to_search = ['Буря', 'мглою', 'небо', 'кроет']
    list_to_search = [k.upper() for k in list_to_search]
    i = (string)
    l = False
    for i in list_to_search:
        if (i == string):
            l = True
            break
    print(l)

string_info()
is_contains()



