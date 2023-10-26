# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44
page = 100
row_page = 50
simv_row = 25
one_simv = 4
var_= 1024
book_ = int(volume_disk//((page * row_page * simv_row * one_simv)/var_**2))
print("Количество книг, помещающихся на дискету:",book_)
