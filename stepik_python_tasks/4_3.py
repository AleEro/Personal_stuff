# https://stepik.org/lesson/23896/step/1?adaptive=true&unit=6422

matrix = ' abcdefghijklmnopqrstuvwxyz'
key = int(input())
print('Result: "' + ''.join([matrix[(matrix.find(l) + key) % 27] for l in input().strip()]) + '"')
