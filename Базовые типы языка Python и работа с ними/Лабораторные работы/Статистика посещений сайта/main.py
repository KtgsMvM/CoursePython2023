users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
dict_ ={"Общее количество": 0, "Уникальные посещения": 0}
users_= len(users)
users_1 = len(set(users))
dict_new={"Общее количество": users_, "Уникальные посещения": users_1}
print(dict_new)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
