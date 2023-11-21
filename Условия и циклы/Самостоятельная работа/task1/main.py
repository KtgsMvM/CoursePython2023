src = not False and True or False and not True

# TODO расписать упрощение выражения

scr = True and True or False and False
scr = True or False
result = scr  # TODO подставить результат выражения

print(src == result)
