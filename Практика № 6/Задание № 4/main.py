class Book:
    title = "Искусство программирования. Том 1"
    author = "Дональд Кнут"
    pages = "722"

book1 = Book()
book1.title = "Искусство программирования. Том 2"
print(dir(book1))
print(book1.title, book1.author, book1.pages, sep=", ")

book2 = Book()
book2.title = "Analysis I"
book2.author = "Terence Tao"
book2.pages = "366"
print(book2.title, book2.author, book2.pages, sep=", ")
