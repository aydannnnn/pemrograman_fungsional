# Percobaan 2 (penerapan single decorators to single function):
# Tulis kembali kode diatas dan tambahkan sebagai decorator pada fungsi say_hi berikut
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        print(make_uppercase)
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    return 'hello there'


say_hi()
