from return_data_file import data_file
from select_row import select_row
from enumerate_data import enumerate_list as enum


def delete_row():
    data, nf = data_file()
    count_rows = len(data)
    if count_rows == 0:
        print("Файл пустой!")
    else:
        number_row = select_row(count_rows)
        del data[number_row - 1]
        data = enum(data)
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data)
        print("Строка успешно удалена!")
