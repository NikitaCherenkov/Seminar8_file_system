from return_data_file import data_file
from select_row import select_row


def change_row():
    data, nf = data_file()
    count_rows = len(data)
    number_row = select_row(count_rows)
    name = input("Введите свое имя: ")
    surname = input("Введите свою фамилию: ")
    birthdate = input("Введите дату рождения: ")
    town = input("Введите город: ")
    data[number_row - 1] = f'{number_row};{name};{surname};{birthdate};{town}\n'
    with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
    print("Данные успешно изменены!")
