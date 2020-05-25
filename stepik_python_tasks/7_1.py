origin_lines = ['4 4', ["..*.",
                        "**..",
                        "..*.",
                        "...."
                        ]]

# test lines
origin_massive = origin_lines[1]
row_count, column_count = (int(i) for i in origin_lines[0].split(' '))

# # считывает количество строк и символов в строке
# row_count, column_count = (int(i) for i in input().split(' '))
#
# # создает массив из количества строк
# origin_massive = [input() for y in range(row_count)]
massive = [[0 for x in range(column_count)] for y in range(row_count)]

# считает звезды вокруг
for row_n in range(row_count):
    for column_n in range(int(column_count)):
        if origin_massive[row_n][column_n] != '*':
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    ai = dx + row_n
                    aj = dy + column_n
                    if 0 <= ai < row_count and 0 <= aj <column_count and origin_massive[ai][aj] == '*':
                        massive[row_n][column_n] += 1
        else:
            massive[row_n][column_n] = '*'
        print(massive[row_n][column_n], end='')
    print('')