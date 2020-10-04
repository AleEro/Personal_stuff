# https://stepik.org/lesson/21299/step/2?adaptive=true&unit=5100

inp = list('aaabccccCCaB')
out = '3ab4c2CaB'
text = input() + "*"
c = 1
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        c += 1
    else:
        print((str(c) if c != 1 else '') + text[i], end='')
        c = 1
