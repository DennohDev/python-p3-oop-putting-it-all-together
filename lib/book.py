#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._page_count = page_count
        self._title = title
    def get_title(self):
        print("Getting title")
        return self._title
    def get_page_count(self):
        print("Getting page")
        return self._page_count
    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    title = property(get_title)
    page_count = property(get_page_count,set_page_count)

# book = Book("And Then There Were None", 272)
# print(book.page_count)
# book.page_count = 200
# print(book.page_count)
# business = Book()
# business.title = "hello"
# print (business.title)