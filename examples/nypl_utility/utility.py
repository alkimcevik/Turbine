from seleniumbase import BaseCase
from examples.nypl_pages.page_homepage_example import HomePage


class NyplUtils(HomePage):

    """a method to check if the values in a dictionary are unique"""
    def check_unique_values(self, dictionary):
        book_set = set()  # creating a set() to add the book names later
        # for loop to go over the elements of the 'dictionary' parameter to check if they are unique
        # if they are unique, they will be added to the 'book_set' set
        for book in dictionary.values():
            print(book)
            if book in book_set:
                return False
            book_set.add(book)
        return True
