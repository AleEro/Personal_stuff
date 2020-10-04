lst = [1, 2, 3, 4, 5, 6]


def modify_list(lst):
    lst[:] = [i // 2 for i in lst if i % 2 == 0]


print('None = ', modify_list(lst))  # None
print('list', lst)  # [1, 2, 3]
modify_list(lst)
print('list', lst)  # [1]

lst = [1, 2, 3, 3, 4, 4, 5]

modify_list(lst)
print('list', lst)  # [5, 4]
