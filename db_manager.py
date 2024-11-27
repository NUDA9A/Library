import json

from book import Book


class DBManager:
    def __init__(self, file):
        # Читает json, создает на основе записей экземпляры Book и добавляет в список, а так же устанавливает текущий id
        self._file = file
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self._books = []
            for book in data:
                self._books.append(
                    Book(
                        book['BookID'],
                        book['Title'],
                        book['Author'],
                        book['Year'],
                        book['Status']
                    )
                )
        if len(self._books) != 0:
            self._id = max(book.id for book in self._books)
        else:
            self._id = 0

    def get_books(self):
        return self._books

    def create_book_write(self, book):
        # Добавляет новую книгу в список, устанвливая ей корректный id и перезаписывает json
        self._id += 1
        book.id = self._id
        self._books.append(book)
        self._save()

    def get_books_by_title(self, book_title):
        books_by_title = []
        for book in self._books:
            if book.title.lower() == book_title:
                books_by_title.append(book)

        return books_by_title

    def get_book_by_id(self, book_id):
        for book in self._books:
            if book.id == book_id:
                return book

        return None

    def update_book_status(self, book, new_status):
        book.status = new_status
        self._save()

    def delete_book(self, book):
        self._books.remove(book)
        self._id = max(book.id for book in self._books)
        self._save()

    def get_books_by_author(self, author):
        books_by_author = []
        for book in self._books:
            if book.author.lower() == author:
                books_by_author.append(book)

        return books_by_author

    def get_books_by_year(self, year):
        books_by_year = []
        for book in self._books:
            if book.year == year:
                books_by_year.append(book)

        return books_by_year

    def _save(self):
        # Перезаписывает json на основе текущего self._books
        with open(self._file, 'w', encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self._books], f, ensure_ascii=False, indent=4)

