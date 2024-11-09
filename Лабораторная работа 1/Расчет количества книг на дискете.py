# TODO Найдите количество книг, которое можно разместить на дискете

size_in_mb = 1.44
pages = 100
lines = 50
symbols = 25

size_book = pages * lines * symbols * 4
size_in_b = size_in_mb * 1024 ** 2

count = size_in_b / size_book

print(f"Количество книг, помещающихся на дискету: {count:.0f}")
