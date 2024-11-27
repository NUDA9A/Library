from book import Book
from db_manager import DBManager
from table_formater import *

db = DBManager("library.json")

books = db.get_books()

display(books)


def get_user_ans(message, l, r):
    # Просит пользователя ввести номер действия и проверяет на корректность
    print(message)
    ans = ""
    while ans == "":
        ans = input("(Для выбора введите номер действия): ")
        if not ans.isdigit() or int(ans) < l or int(ans) > r:
            ans = ""
            print("Вы ввели недопустимое значение, попробуйте еще раз!")
    return ans


def get_id_input():
    # Просит пользователя ввести id и проверяет что id корректный, а так же, что есть книга с таким id
    id_inp = ""
    while id_inp == "":
        id_inp = input("Введите id книги: ")
        if id_inp == "":
            return None
        if not id_inp.isdigit():
            id_inp = ""
            print("Вы ввели недопустимый id,"
                  " попробуйте еще раз, либо нажмите Enter при вводе для выхода из действия")
            continue
        book_by_id = db.get_book_by_id(int(id_inp))
        if book_by_id is None:
            id_inp = ""
            print("Такой книги нет, попробуйте еще раз, либо нажмите Enter при вводе для выхода из действия")
            continue
    return book_by_id


while True:
    menu_message = """
        Приветствуем в нашей библиотеке!
        Выберите действие:
        1. Добавить книгу
        2. Получить книгу
        3. Изменить статус книги
        4. Удалить книгу
        5. Отоброзить список всех книг
        6. выйти
        """
    ans = get_user_ans(menu_message, 1, 6)

    if ans == "1":
        title = input("Введите название книги: ")
        author = input("Введите имя автора: ")
        year = ""
        while year == "":
            year = input("Введите год написания: ")
            if not year.isdigit():
                year = ""
                print("Год должен быть числом!")
        db.create_book_write(Book(0, title, author, int(year), "в наличии"))
    elif ans == "2":
        type_message = """
                Выберите действие:
                1. Найти по названию
                2. Найти по автору
                3. Найти по году написания
                4. Выйти
                """
        type = get_user_ans(type_message, 1, 4)
        if type == "1":
            books = db.get_books_by_title(input("Введите название книги: "))
            if len(books) == 0:
                print("Нет книг с таким названием!")
                input("Нажмите Enter для продолжения")
                continue
            display(books)
            input("Нажмите Enter для продолжения")
        elif type == "2":
            books = db.get_books_by_author(input("Введите имя автора: "))
            if len(books) == 0:
                print("Нет книг с таким автором!")
                input("Нажмите Enter для продолжения")
                continue
            display(books)
            input("Нажмите Enter для продолжения")
        elif type == "3":
            books = db.get_books_by_year(int(input("Введите год написания книги: ")))
            if len(books) == 0:
                print("Нет книг с такой датой написания!")
                input("Нажмите Enter для продолжения")
                continue
            display(books)
            input("Нажмите Enter для продолжения")
        else:
            continue
    elif ans == "3":
        b = get_id_input()
        if b is None:
            continue
        status_message = """
        Выберите статус:
        1. В наличии
        2. Выдана
        3. Выйти
        """
        status = get_user_ans(status_message, 1, 3)
        if status == "1":
            db.update_book_status(b, "в наличии")
        elif status == "2":
            db.update_book_status(b, "выдана")
        else:
            continue

    elif ans == "4":
        b = get_id_input()
        if b is None:
            continue
        db.delete_book(b)

    elif ans == "5":
        display(db.get_books())
        input("Нажмите Enter для продолжения")
        continue

    elif ans == "6":
        break

