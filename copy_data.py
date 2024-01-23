from return_data_file import data_file
from select_row import select_row
from enumerate_data import enumerate_list as enum


def copy_row():
    print("Укажите номер файла, из которого будет производиться копирование\n")
    data_input, nf_input = data_file()
    number_row_input = int(select_row(len(data_input)))
    print(f"\nВыбранная строка: {data_input[number_row_input - 1]}")
    if nf_input == 1:
        data_output, nf_output = data_file(2)
    elif nf_input == 2:
        data_output, nf_output = data_file(1)
    print("Укажите номер строки, на которую будут помещены данные\n")
    number_row_output = int(select_row(len(data_output) + 1))
    data_output.insert(number_row_output - 1, data_input[number_row_input - 1])
    data_output = enum(data_output)
    with open(f'db/data_{nf_output}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data_output)
    print("Строка успешно скопирована")
    not_del_original = -1
    while not_del_original > 1 or not_del_original < 0:
          not_del_original = int(input(f"Удалить скопированную строку (№ {number_row_input}) в исходном файле?\n"
                                       f"1. Да\n"
                                       f"2. Нет\n"
                                       f"Выбор: ")) - 1
    if not not_del_original:
        data_input.pop(number_row_input - 1)
        data_input = enum(data_input)
        with open(f'db/data_{nf_input}.txt', 'w', encoding='utf-8') as file:
            file.writelines(data_input)
        print("Исходная строка удалена")
