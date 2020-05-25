#https://stepik.org/lesson/21211/step/2?adaptive=true&unit=5097

def f(name):
    return name


list1 = []
input_value_list = [5, [5, 12, 9, 20, 12]]
dictionary = {}
for input_value in range(int(input())):
    a = int(input())
    list1.append(a)
    if a not in dictionary:
        dictionary[a] = f(a)


for i in list1:
    print(dictionary[i])