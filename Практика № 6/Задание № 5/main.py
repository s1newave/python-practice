from book import Book


class Bookshelf:
    max_books = 3
    books = []

    def add_book(self, book):
        if len(self.books) < self.max_books:
            self.books.append(book)
            print(f"Книга с названием \"{book.title}\" добавлена!")
        else:
            print("Книжная полка заполнена! Книга не добавлена.")

    def remove_book(self, title):
        for i in range(len(self.books)):
            if title == self.books[i].title:
                del self.books[i]
                print(f"Книга с названием \"{title}\" удалена!")
                return
        print(f"Книга с названием \"{title}\" не найдена!")

    def show_books(self):
        print("Книги на книжной полке:")
        for book in self.books:
            print(book.author, book.title, book.pages, sep=", ")

    def get_total_pages(self):
        return sum([book.pages for book in self.books])


bookshelf = Bookshelf()

bookshelf.add_book(Book("1984", "Джордж Оруэлл", 320))
bookshelf.add_book(Book("Десять негритят", "Агата Кристи", 288))
bookshelf.add_book(Book("Изучаем Python", "Марк Лутц", 1280))
bookshelf.add_book(Book("Невероятные приключения ДжоДжо. Часть 1: Призрачная кровь", "Хирохико Араки", 182))
print()

bookshelf.show_books()
print(f"Количество страниц на полке: {bookshelf.get_total_pages()}")
print()

bookshelf.remove_book("1984")
bookshelf.show_books()