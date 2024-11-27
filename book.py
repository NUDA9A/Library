class Book:
    def __init__(self, id, title, author, year, status):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self):
        # Возвращает книгу в виде словаря для удобного добавления в json
        return {
            "BookID": self.id,
            "Title": self.title,
            "Author": self.author,
            "Year": self.year,
            "Status": self.status
        }
