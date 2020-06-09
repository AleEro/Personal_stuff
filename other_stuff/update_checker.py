# import csv
import re
# import pandas as pd
import http
from openpyxl import load_workbook

xlsx = r'C:\Users\Z510\Downloads\Текущий прогресс.xlsx'

# - openpyxl
wb = load_workbook(filename=xlsx)
ws = wb.active
# data = ws.values

# все это полная ъуета
# todo: добавить http запрос на стим и диск
# todo: добавить столбец в таблицу:
#     имя - updates_autodetect
#     если есть - перезаписывать


def First_column_parser(matchstr):
    # print(matchstr)
    # if 'steam'in matchstr:
    rawstr = r'"([^",]*)"' # rawstr for steam services
    # else:
    #     rawstr = r'([\w ]*)'
    match_obj = re.search(rawstr, matchstr)
    return match_obj


# Print row per row
for cellObj in ws:
    for cells in cellObj:
        if cells.value is None:
            pass
        else:
            if 'A' in cells.coordinate and 'steam' in cells.value:
                print(cells.coordinate.split())
                print(First_column_parser(cells.value))
# - -



#
# rawstr = r""""(.*)","(.*)""""
# embedded_rawstr = r""""(.*)","(.*)""""
# matchstr = """
# A74 =HYPERLINK("https://steamcommunity.com/sharedfiles/filedetails/?id=1442128058","Intelligence and Espionage")
# "Название"
# A75 =HYPERLINK("https://steamcommunity.com/sharedfiles/filedetails/?id=924990631","Ultimate Technologies")
# A76 =HYPERLINK("https://steamcommunity.com/sharedfiles/filedetails/?id=1711098117","PJs :: Better Megastructures")
# A77 =HYPERLINK("https://steamcommunity.com/sharedfiles/filedetails/?id=1603330813","Ecology Mod")
# A78 =HYPERLINK("https://steamcommunity.com/sharedfiles/filedetails/?id=1771786608","AlphaMod")
# """
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
# group_2 = match_obj.group(2)

