calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    string = (len(string), string.upper(), string.lower())
    print(string)

def is_contains(string, list_to_search):
    count_calls()
    string = string.upper()
    list_to_search = [k.upper() for k in list_to_search]
    l = False
    for i in list_to_search:
        if (i == string):
            l = True
    print(l)

string_info('Чем больше я знаю, тем больше понимаю, что не знаю ничего')

is_contains('НеБо', ('Буря', 'мглою', 'небо', 'кроет'))

print(calls)





