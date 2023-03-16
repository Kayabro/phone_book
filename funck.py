def open_file():
    with open('phone_book', 'r', encoding='utf-8') as data:
        file = data.readlines()
        for i in file:
            print(*i.split(';'))
def save_file():
    pass
def show_file():
    pass
def add_file():
    with open('phone_book', 'a', encoding='utf-8') as data:
        user_input = input('Введите данные имя,фамилия, номер и комментарий, через пробел: ')
        data.write(user_input)
def diff_file():
    pass
def serch_file():
    pass
def delete_conact_file():
    pass

