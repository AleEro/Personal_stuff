# import csv
import re
# import pandas as pd
import requests
from openpyxl import load_workbook

xlsx = r'C:\Users\Z510\Downloads\Текущий прогресс.xlsx'

# - openpyxl
wb = load_workbook(filename=xlsx)
ws = wb.active
# data = ws.values


def get_http(url):
    return requests.get(url)


def parse_http(http):
    pass


def first_column_parser(matchstr):
    # - future features
    # # print(matchstr)
    # # if 'steam'in matchstr:
    # rawstr = r'"([^",]*)"'  # raw string for steam services
    # # else:
    # #     rawstr = r'([\w ]*)'
    # match_obj = re.search(rawstr, matchstr)
    # - -

    match_obj = re.search(r'"([^",]*)"', matchstr)  # raw string for steam services
    return match_obj.group(1)

# все это полная ъуета
# todo: добавить http запрос на стим и диск
# todo: добавить столбец в таблицу:
#     имя - updates_autodetect
#     если есть - перезаписывать


# Print row per row
for cellObj in ws:
    for cells in cellObj:
        if cells.value is None:
            continue
        else:
            if 'A' in cells.coordinate and 'steam' in cells.value:

                print(get_http(first_column_parser(cells.value)), cells.coordinate.split())
                # print(first_column_parser(cells.value), cells.coordinate.split())

# add new column
ws.insert_cols(2)
# изменить имя колонки
# ws.insert_cols(2)

# # print all in worksheet (ws)
for cellObj in ws:
    for cells in cellObj:
        print(cells.value, end=' ')
        print(cells.coordinate, end=' / ')
    print('-- END --')

# - -

# import re
#
# # common variables
#
# rawstr = r"""<div class="detailsStatsContainerRight"><div class="detailsStatRight">.*</div><div class="detailsStatRight">.*</div><div class="detailsStatRight">(.*)</div></div>"""
# embedded_rawstr = r"""<div class="detailsStatsContainerRight"><div class="detailsStatRight">.*</div><div class="detailsStatRight">.*</div><div class="detailsStatRight">(.*)</div></div>"""
# matchstr = """<div class="detailsStatsContainerRight"><div class="detailsStatRight">120.814 MB</div><div class="detailsStatRight">1 мар. 2018 в 17:14</div><div class="detailsStatRight">23 июл. 2019 в 15:48</div></div>"""
#
# # method 1: using a compile object
# compile_obj = re.compile(rawstr)
# match_obj = compile_obj.search(matchstr)
#
# # method 2: using search function (w/ external flags)
# match_obj = re.search(rawstr, matchstr)
#
# # method 3: using search function (w/ embedded flags)
# match_obj = re.search(embedded_rawstr, matchstr)
#
# # Retrieve group(s) from match_obj
# all_groups = match_obj.groups()
#
# # Retrieve group(s) by index
# group_1 = match_obj.group(1)
#
