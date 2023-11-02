field = [  # поле 3x3 с крестиками и ноликами
    ["X", "0", "X"],  # первая строка таблицы
    ["O", "X", "O"],  # вторая строка таблицы
    ["X", "O", "X"],  # третья строка таблицы
]

for row in field:  # Перебираем каждый внутренний список, представляющий строку таблицы
    for cell in row:  # Перебираем каждый элемент внутреннего списка, представляющий ячейку таблицы
        print(cell, end=" ")  # `end=" "` позволяет выводить значения в одной строке, а не на отдельной
    print()  # Выводим пустую строку с помощью `print()`, чтобы перейти на новую строку и распечатать следующую строку таблицы.
