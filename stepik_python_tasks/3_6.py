variable_count = 8
# variable_count = int(input())
var = ''
counter = 0
while counter < variable_count:
    counter += 1
    var += (str(counter) * counter)
var = ' '.join(var)
print(var[:(variable_count*2)])
