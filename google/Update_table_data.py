from Google_API import *
from Steam_API import *
import datetime


def test_get_values():
    ss = Spreadsheet()
    # values = ss.get_values('1iGcBdQN-Vbr0ZKjrHJ-WlMvdwWesxg1FgSCW7Jh6KZE', tb_min=1, tb_max=75)
    values = ss.get_values('1WZoO5ntxYfqFXuuJCaWuz_ullyT-9zbSdf2I5uhkXik', tb_min=1, tb_max=75)
    if values[0][2] != 'Аutomatic Script Update':
        ss.insert_dimension(2, 3)
        ss.prepare_setValue('C1', [['Аutomatic Script Update']])
    ss.prepare_setValue('C2', [[f'{datetime.date.today()}']])

    counter = 0
    for value in values:
        counter += 1
        if value != [] and 'steam' in value[0]:
            link = value[0].split('"')
            try:
                print(counter, link[3], steam_get(link[1]))
                ss.prepare_setValue(f'C{counter}', [[steam_get(link[1])]])
            except KeyError:
                ss.prepare_setValue(f'C{counter}', [['ERROR']])
    ss.runPrepared()

if __name__ == '__main__':
    test_get_values()
