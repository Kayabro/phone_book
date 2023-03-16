def print_menu():
        while True:
            print('Это телефонный справочник, вот что он умеет: \n',
                  '1. Открыть файл\n',
                  '2. Сохранить файл\n',
                  '3. Показать контакты\n',
                  '4. Добавить новый контакт\n',
                  '5. Изменить существующий контакт\n',
                  '6. Найти контакт по одному параметру\n',
                  '7. Удалить контакт\n',
                  '8. Закрыть файл')
            print('')
            print('Используя цифру от 1 до 8, выберите действие')
            print("")
            act = input('Какое действие выполнить: ')
            if act.isdigit() == True:
                if 1 <= int(act) <= 8:
                    return int(act)
                else:
                    print('Цифра должна быть от 1 до 8!')
            else:
                print('Выбрать можно только цифрой от 1 до 8!')

import funck

while True:
    user_choic = print_menu()
    match user_choic:
        case 1:
            funck.open_file()
        case 2:
            print('2')
        case 3:
            print('3')
        case 4:
            funck.add_file()
        case 5:
            print('5')
        case 6:
            print('6')
        case 7:
            print('7')
        case 8:
            print('Досвидос!')
            break
