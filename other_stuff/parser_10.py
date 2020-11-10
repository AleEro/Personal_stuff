# -*- Encoding: utf-8 -*-
import re
import os
from time import strftime
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)


def count(item1, item2):
    counter = 0
    try:
        if item1 == item2:
            counter += 1
    except ValueError:
        pass
    return counter


def parse_file(file_name, raw_str=r'''(?P<key>[A-Za-z._0-9 ]*)(:[0-9 ]+)(?P<value>".+")''', file_encoding="utf-8-sig"):
    print('\nfile_name: ', file_name,
          '\nraw_str: ', raw_str,
          '\nencoding: ', file_encoding,
          '\nfile: \n')

    with open(file_name, "r", encoding=file_encoding) as stream:
        match_str = stream.read()
        parse_result = re.findall(raw_str, match_str, re.MULTILINE)

    # b = np.array(parse_result)
    # print(b[:, 2])
    # for i in b:
    #     print(i[0], i[2])
    # print('trait_pc_squareworld_habitable_preference_desc' in b[:, 0])
    return parse_result


def merge_3_files(filename_1, filename_2, filename_3):
    old_eng = filename_1
    new_eng = filename_2
    old_rus = filename_3
    filename = f'result{strftime("%H_%M")}.yml'
    print('старых строк', len(filename_1))
    print('новых строк', len(filename_2))
    print('русские строки', len(filename_3))
    with open(filename, 'w', encoding="utf-8-sig") as result_file:
        result_file.write('l_russian:\n')

        for old_rus_line_part in old_rus:
            for old_eng_line_part in old_eng:
                if old_rus_line_part[1].strip() == old_eng_line_part[1].strip():  # if key rus eql key eng
                    if len(old_rus_line_part[2]) < 4:  # if len ru text < 4 replace with eng
                        old_rus_line_part[2] = old_eng_line_part[2]

        # CHECK NEW-OLD BLOCK
        ru_key_list1 = dict()
        eng_file_lines = list()
        replaced_lines = list()
        for i, new_eng_line_part in enumerate(new_eng):  # for new
            new_eng_line_key = new_eng_line_part[0].strip()
            for old_eng_line_part in old_eng:  # for old
                if new_eng_line_part[2] == old_eng_line_part[2]:  # if old txt eql new txt
                    print(i,
                          '\n{0}\n{1}\n=='.format(new_eng_line_key, old_eng_line_part[0].strip()),
                          '\n{0}\n{1}\n=='.format(new_eng_line_part[2], old_eng_line_part[2]),
                          end='\n\n')
                    ru_key_list1[new_eng_line_key] = new_eng_line_part[1]  # for russ vocabulary
                    eng_file_lines.append(new_eng_line_key)  # for escape twice writing
            if new_eng_line_key not in eng_file_lines: # writing correct missed lines
                eng_file_lines.append(new_eng_line_key)
                result_file.write(f' {new_eng_line_key}{new_eng_line_part[1]}{new_eng_line_part[2]}\n')

        # MERGE NEW>RUS
        for old_rus_line_part in old_rus:
            if old_rus_line_part[0].strip() in ru_key_list1:
                result_file.write(
                    f' {old_rus_line_part[0].strip()}{ru_key_list1[old_rus_line_part[0].strip()]}{old_rus_line_part[2]}\n')
                replaced_lines.append(old_rus_line_part)
        print('совпадений с старых живых с русским', len(replaced_lines))

    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    # перепись кодировки с винды на линку
    with open(filename, 'rb') as open_file:
        content = open_file.read()

    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    with open(filename, 'wb') as open_file:
        open_file.write(content)


def compare_2_files(filename_1, filename_2):
    for o, i in enumerate(filename_1):
        for k, j in enumerate(filename_2):
            if i[0].strip() == j[0].strip():
                print('-' * 30)
                print(o, i[0], i[2])
                print(k, j[0], j[2])


def first_call():
    file_1 = 'gigaengineering_l_english.yml'
    file_2 = 'giga_l_english.yml'
    file_3 = 'gigaengineering_l_russian1.yml'

    # filename_1 = input('имя старое (без расширения): ')
    # filename_2 = input('имя нового (без расширения): ')
    # filename_3 = input('Введите имя нового файла (без расширения): ')

    filedata_1 = parse_file(file_name=f'{os.getcwd()}/{file_1}')  # OENG
    filedata_2 = parse_file(file_name=f'{os.getcwd()}/{file_2}')  # NENG
    filedata_3 = parse_file(file_name=f'{os.getcwd()}/{file_3}')  # ORUS

    print(f'\n\nКаталог исполнения скрипта:\n{os.getcwd()}\n')
    # compare_2_files(filedata_1, filedata_2)
    merge_3_files(filedata_1, filedata_2, filedata_3)
    return print("\nFINISHED")


if __name__ == '__main__':
    first_call()
