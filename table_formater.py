def _format_row(row_data, widths):
    return "|".join(f" {str(data).center(width)} " for data, width in zip(row_data, widths))


def _generate_separator(widths):
    return "+".join("-" * (width + 2) for width in widths)


def _calculate_column_widths(books):
    # Находит наибольшую длину для каждого столбца
    headers = ["ID", "Название", "Автор", "Год", "Статус"]
    widths = [
        max(len(str(book.id)) for book in books) if books else 0,
        max(len(book.title) for book in books) if books else 0,
        max(len(book.author) for book in books) if books else 0,
        max(len(str(book.year)) for book in books) if books else 0,
        max(len(book.status) for book in books) if books else 0,
    ]
    widths = [max(len(header), width) for header, width in zip(headers, widths)]
    return headers, widths


def display(books):
    # Выводит в красивом виде табличку с книгами
    headers, widths = _calculate_column_widths(books)
    separator = _generate_separator(widths)

    print(_format_row(headers, widths))
    print(separator)

    for book in books:
        row_data = [
            book.id,
            book.title,
            book.author,
            book.year,
            book.status,
        ]
        print(_format_row(row_data, widths))
        print(separator)
