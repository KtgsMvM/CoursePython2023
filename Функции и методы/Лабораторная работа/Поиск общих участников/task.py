# TODO Напишите функцию find_common_participants
 # надо стараться писать универсальные функции
def find_common_participants(str1_: str, str2_:str, sep=","):# передаем в функцию  две строки, заменяем разделитель на запятую
    # чтобы найти одинаковые элементы используем объединение множеств и превращаем строки в множества
    str1_ = set(str1_.split(sep)) # разделить строки по разделителю, превратить в множество
    str2_ = set(str2_.split(sep))
    #результат записываем в виде списка состоящего из одинаковых элементов
    result = list(str1_.intersection(str2_))
    result.sort() # сортируем результат (полученные элементы) по алфавиту
    return result #  перезаписываем результат

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, # выводим результат черезвызываем созданную функцию
                         participants_second_group,
                         sep="|"))# исключая разделители "|"
        # print ("Одинаковые фамилии:","i")
# TODO Провеьте работу функции с разделителем отличным от запятой
