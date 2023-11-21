list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min_value_index = 0
min_value = list_[min_value_index]

# TODO заменить на enumerate
# for current_value in list_:
#    # current_value = list_[i]
#    if current_value <= min_value:
#        min_value = current_value
#        min_value_index = i
res = []

for current_index, current_value in enumerate(list_):
    if current_value <= min_value:
        min_value = current_value
        min_value_index = current_index
        if min_value in res or not res:
            res.append(min_value)
        else:
            res = [min_value]


# print(res)
# for min_value_index, min_value in res:
print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)

# for current_index, current_value in enumerate(list_):
#     if current_value <= min_value:
#         min_value = current_value
#         min_value_index = current_index
#
#
#
#     print("Индекс:", min_value_index, "->", "Значение:", min_value)