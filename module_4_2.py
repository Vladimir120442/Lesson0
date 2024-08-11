def test_function():
    def inner_function():
        a = "Я в области видимости функции test_function"
        print(a)
    inner_function()


test_function()
#inner_function()