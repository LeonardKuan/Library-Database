class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, genre):
        if title not in self.books:
            self.books[title] = {'author': author, 'genre': genre}
            print(f'Book "{title}" added to the library.')
        else:
            print(f'Book "{title}" already exists in the library.')

    def remove_book(self, title):
        if title in self.books:
            del self.books[title]
            print(f'Book "{title}" removed from the library.')
        else:
            print(f'Book "{title}" not found in the library.')

    def update_book(self, title, author=None, genre=None):
        if title in self.books:
            if author is not None:
                self.books[title]['author'] = author
            if genre is not None:
                self.books[title]['genre'] = genre
            print(f'Book "{title}" updated.')
        else:
            print(f'Book "{title}" not found in the library.')

    def display_books(self):
        if not self.books:
            print('The library is empty.')
        else:
            print('Library Books:')
            for title, info in self.books.items():
                print(f'Title: {title}, Author: {info["author"]}, Genre: {info["genre"]}')


# Example Usage:
library = Library()

library.display_books()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
library.add_book("To Kill a Mockingbird", "Harper Lee", "Drama")

library.display_books()

library.update_book("The Great Gatsby", author="Francis Scott Fitzgerald")
library.remove_book("To Kill a Mockingbird")

library.display_books()
