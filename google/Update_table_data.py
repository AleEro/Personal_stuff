from Google_API import *
from Steam_API import *
import datetime


def test_get_values():
    ss = Spreadsheet()
    values = ss.get_values('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_min=1, tb_max=75)
    if values[0][2] != 'Аutomatic Script Update':
        ss.insert_dimension(2, 3)
        ss.prepare_setValue('C1', [['Аutomatic Script Update']])
    ss.runPrepared()
    ss.prepare_setValue('C2', [[f'{datetime.date.today()}']])

    counter = 0
    for value in values:
        counter += 1
        if value != [] and 'steam' in value[0]:
            link = value[0].split('"')
            # print(counter, link[1], link[3])
            # print(value)
            try:
                print(counter, link[3], steam_get(link[1]))
                ss.prepare_setValue(f'C{counter}', [[steam_get(link[1])]])
                ss.runPrepared()

            except KeyError:
                ss.prepare_setValue(f'C{counter}', [['ERROR']])
                ss.runPrepared()

# ss.prepare_setValue("C1", [['Аutomatic Script Update'],
#                            ['Аutomatic Script Update'],
#                            ['Аutomatic Script Update'],
#                            ['Аutomatic Script Update'],
#                            ['Аutomatic Script Update']])
# ss.runPrepared()


# def steam_talking():
#     pass
#
# # # ss - экземпляр нашего класса Spreadsheet
# ss = Spreadsheet()
# # ss.create_table()
# #  https://docs.google.com/spreadsheets/d/1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE/edit?usp=sharing
# # ss.get_table('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE')
# # ss.get_data('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_max=6, tb_min=16)
# # ss.get_data('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_max=23, tb_min=57)
# ss.get_values('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_min=6, tb_max=76)
# # ss.give_access()
# # ss.prepare_setColumnWidth(0, 317)
# # ss.prepare_setColumnWidth(1, 200)
# # ss.prepare_setColumnsWidth(2, 3, 165)
# # ss.prepare_setColumnWidth(4, 100)
# # ss.prepare_setValues("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
# # ss.prepare_setValues("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], "COLUMNS")
# # ss.insert_dimension(2, 3)

# ss.runPrepared()

if __name__ == '__main__':
    test_get_values()
