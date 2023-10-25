# TODO Найдите количество книг, которое можно разместить на дискете
a = 1.44
b = 100
c = 50
d = 25
f = 4
var_= 1024
disk_ = float(a)
kol_ctn = int(b)
kol_ctk = int(c)
cimv_ctk = int(d)
inf_cimv = int(f)
book_ = int(disk_//((kol_ctn * kol_ctk * cimv_ctk * inf_cimv)/var_**2))
print("Количество книг, помещающихся на дискету:", book_)
