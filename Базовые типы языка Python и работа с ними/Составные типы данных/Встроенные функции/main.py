list_digit: list[int] = [4,9,5,1,8,4]
print(list_digit)
print("Сумма цифр", sum(list_digit))
print("Количество цифр", len(list_digit))
print("Минимальная цифра", min(list_digit))
print("Максимальная цифра", max(list_digit))
mean_list = sum(list_digit)/len(list_digit)
print("Среднее арифметическое цифр", round(mean_list, 2))
