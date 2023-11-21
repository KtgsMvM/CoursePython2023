# TODO Напишите функцию find_common_participants

def find_common_participants(str1_: str, str2_:str, sep=","):
    str1_ = set(str1_.split(sep))
    str2_ = set(str2_.split(sep))
    result = list(str1_.intersection(str2_))
    result.sort()
    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,
                         participants_second_group,
                         sep="|"))
        # print ("Одинаковые фамилии:","i")
# TODO Провеьте работу функции с разделителем отличным от запятой
