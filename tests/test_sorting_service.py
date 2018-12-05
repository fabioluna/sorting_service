import unittest
from sorting_service.sorting_service import sorting_service


books = [
    {
        "number": 1,
        "tittle": "Java How to Program",
        "author": "Deitel & Deitel",
        "edition": 2007,
    },
    {
        "number": 2,
        "tittle": "Patterns of Enterprise Application Architecture",
        "author": "Martin Fwoler",
        "edition": 2002,
    },
    {
        "number": 3,
        "tittle": "Head First Design Patterns",
        "author": "Elisabeth Freeman",
        "edition": 2004,
    },
    {
        "number": 4,
        "tittle": "Internet & WWW: How to Program",
        "author": "Deitel & Deitel",
        "edition": 2007,
    },
]


class TestSortingService(unittest.TestCase):
    def test_case_one(self):
        books_sorted = sorting_service(books)
        list_number = [x["number"] for x in books_sorted]
        expected_result = [3, 4, 1, 2]
        self.assertEqual(list_number, expected_result)

    def test_case_two(self):
        keys = [
            {"key": "author", "reverse": False},
            {"key": "tittle", "reverse": True},
        ]
        books_sorted = sorting_service(books, keys)
        list_number = [x["number"] for x in books_sorted]
        expected_result = [1, 4, 3, 2]
        self.assertEqual(list_number, expected_result)

    def test_case_three(self):
        keys = [
            {"key": "edition", "reverse": True},
            {"key": "author", "reverse": True},
            {"key": "tittle", "reverse": False},
        ]
        books_sorted = sorting_service(books, keys)
        list_number = [x["number"] for x in books_sorted]
        expected_result = [4, 1, 3, 2]
        self.assertEqual(list_number, expected_result)

    def test_case_four(self):
        self.assertRaises(
            Exception, sorting_service, "A set of books can't be null."
        )

    def test_case_five(self):
        books_sorted = sorting_service([])
        expected_result = []
        self.assertEqual(books_sorted, expected_result)
