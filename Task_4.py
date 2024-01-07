entry = input("Введите название книги, автора и год издания.").split(", ")
title = entry[0]
author_name = entry[1].split(" ")[0]
author_surname = entry[1].split(" ")[1]
year = entry[2]

print("{}, {}. {}. {}.".format(author_surname, author_name, title, year))
print("%s, %s. %s. %s." % (author_surname, author_name, title, year))
print(f"{author_surname}, {author_name}. {title}. {year}.")