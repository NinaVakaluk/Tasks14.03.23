# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def choice(phone):
    while True:
        print('Выберите необходимые действия?')
        user_choice = input('1 -Найти контакт\n2 - Добавить контакт\n\
3 - Изменить контакт\n4 - Удалить контакт\n5 - Просмотреть все контакты\n0 - Закончить работу\n')
        print()
        
        if user_choice == '1':
            spisok_contaktov =  read(phone)
            find_number(spisok_contaktov)
        elif user_choice == '2':
            phone_num_add(phone)
        elif user_choice == '3':
            number_change(phone)
        elif user_choice == '4':
            delete_contact(phone)
        elif user_choice == '5':
            view_number(phone)
        elif user_choice == '0':
            print('Выход!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue

def   read(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    spisok_contaktov = []
    for line in lines:
        line = line.strip().split()
        spisok_contaktov.append(dict(zip(headers, line)))
    return spisok_contaktov


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        spisok_contaktov = []
        for line in file.readlines():
            spisok_contaktov.append(line.split())
    return spisok_contaktov


def search_parameters():
    print('Что изменить?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(spisok_contaktov):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in spisok_contaktov:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def phone_num_add(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def view_number(file_name):
    list_of_contacts = sorted(read(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(spisok_contaktov: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in spisok_contaktov:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def number_change(file_name):
    spisok_contaktov = read_file_to_list(file_name)
    number_to_change = search_to_modify(spisok_contaktov)
    spisok_contaktov.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    spisok_contaktov.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in spisok_contaktov:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    spisok_contaktov = read_file_to_list(file_name)
    number_to_change = search_to_modify(spisok_contaktov)
    spisok_contaktov.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in spisok_contaktov:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(spisok_contaktov: list):
    for contact in spisok_contaktov:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'phone.txt'
    choice(file)