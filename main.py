from core.search_helper import SearchHelper
from core.baseapp import BaseApp
from view.view_book import ViewBook
from view.input_book import InputBook


class MainApp(BaseApp):
    def __init__(self):
        self.books = []


if __name__ == "__main__":
    app = MainApp()
    app.run()


def list_book(self):
    view = ViewBook(self.books)
    view.list()


def add_book(self):
    add = InputBook()
    add.input()


def search_book():
    cari = InputBook()
    cari.search()
    help = SearchHelper()
    help.search_title()
    liat = ViewBook(books=self)
    liat.list()
