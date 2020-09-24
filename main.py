from core.search_helper import SearchHelper
from core.baseapp import BaseApp
from view.view_book import ViewBook
from view.input_book import InputBook


class MainApp(BaseApp):
    def __init__(self, books=[]):
        self.books = books

    def list_book(self):
        liat = ViewBook
        liat.list(self)

    def add_book(self):
        add = InputBook()
        add.input()

    def search_book(self):
        cari = InputBook()
        cari.search()
        help = SearchHelper()
        help.search_title()
        liat = ViewBook(books=self)
        liat.list()


if __name__ == "__main__":
    app = MainApp()
    app.run()
