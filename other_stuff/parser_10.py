# -*- Encoding: utf-8 -*-
import re
import os
from time import strftime


def parse_file(file_name, raw_str=r'''(?P<key>[A-Za-z._0-9 ]*)(:[0-9 ]+)(?P<value>".+")''', file_encoding="utf-8-sig"):
    print('\nfile_name: ', file_name,
          '\nraw_str: ', raw_str,
          '\nencoding: ', file_encoding,
          '\nfile: \n')

    with open(file_name, "r", encoding=file_encoding) as stream:
        match_str = stream.read()
        parse_result = re.findall(raw_str, match_str, re.MULTILINE)

    return parse_result


def compare(filename_1, filename_2, filename_3):
    b = filename_1
    d = filename_2
    f = filename_3
    filename = f'result{strftime("%H_%M")}.yml'
    print('старых строк', len(filename_1))
    print('новых строк', len(filename_2))
    print('русские строки', len(filename_3))
    with open(filename, 'w', encoding="utf-8-sig") as result_file:
        result_file.write('l_russian:\n')
        list1 = dict()
        list2 = list()
        key_list2 = list()
        for i, item_d in enumerate(d):
            item_d_s = item_d[0].strip()
            for item_b in b:
                if item_d[2] == item_b[2]:
                    list1[item_d_s] = item_d[1]  # for russ vocabulary
                    list2.append(item_d_s)  # for escape twice writing
            if item_d_s not in list2:
                list2.append(item_d_s)
                result_file.write(f' {item_d_s}{item_d[1]}{item_d[2]}\n')  # writing correct missed lines
            print(i, item_d_s)

        for item_f in f:
            if item_f[0].strip() in list1:
                print(item_f[0].strip())
                result_file.write(f' {item_f[0].strip()}{list1[item_f[0].strip()]}{item_f[2]}\n')
                key_list2.append(item_f)

        print('совпадений с старых живых с русским', len(key_list2))

    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    # перепись кодировки с винды на линку
    with open(filename, 'rb') as open_file:
        content = open_file.read()

    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    with open(filename, 'wb') as open_file:
        open_file.write(content)


def first_call():
    filename_1 = 'gigaengineering_l_english.yml'
    filename_2 = 'giga_l_english.yml'
    filename_3 = 'gigaengineering_l_russian1.yml'

    # filename_1 = input('имя старое (без расширения): ')
    # filename_2 = input('имя нового (без расширения): ')
    # filename_3 = input('Введите имя нового файла (без расширения): ')

    filedata_1 = parse_file(file_name=f'{os.getcwd()}/{filename_1}')  # OENG
    filedata_2 = parse_file(file_name=f'{os.getcwd()}/{filename_2}')  # NENG
    filedata_3 = parse_file(file_name=f'{os.getcwd()}/{filename_3}')  # ORUS

    print(f'\n\nКаталог исполнения скрипта:\n{os.getcwd()}\n')
    compare(filedata_1, filedata_2, filedata_3)
    return print("\nFINISHED")


if __name__ == '__main__':
    first_call()
