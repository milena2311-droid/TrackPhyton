# TODO Найдите количество книг, которое можно разместить на дискете
memory_disk = 1.44
amount_lists = 100
amount_line = 50
amount_symdols = 25
amount_bytes = 4

memory_book = amount_bytes * amount_symdols * amount_line * amount_lists
memory_book1 = memory_book / 1024 / 1024
amount_books = memory_disk // memory_book1
print("Количество книг, помещающихся на дискету:", int(amount_books))
