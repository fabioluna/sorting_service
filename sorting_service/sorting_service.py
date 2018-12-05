def sorting_service(books, keys=[{"key": "tittle", "reverse": False}]):
    try:
        if len(keys) > 1:
            books = sorting_service(books, keys[1 : len(keys)])

        books_sorted = sorted(
            books, key=lambda x: x[keys[0]["key"]], reverse=keys[0]["reverse"]
        )

        return books_sorted

    except TypeError:
        raise Exception("A set of books can't be null.")
