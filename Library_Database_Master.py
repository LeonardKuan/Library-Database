import tkinter as tk
from tkinter import messagebox
import random
import string

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        if self.books:
            for k in range(len(self.books)):
                if title == self.books[k]["title"] and author == self.books[k]["author"] and genre == self.books[k]["genre"]:
                    self.books[k]["count"] += 1
                    break
                if k == len(self.books) - 1:
                    self.books.append({"title": title, "author": author, "genre": genre, "count": 1})
        else:
            self.books.append({"title": title, "author": author, "genre": genre, "count": 1})

    def remove_book(self, title, author, genre):
        if self.books:
            for k in range(len(self.books)):
                if title == self.books[k]["title"] and author == self.books[k]["author"] and genre == self.books[k]["genre"]:
                    if self.books[k]["count"] == 1:
                        del self.books[k]
                    else:
                        self.books[k]["count"] -= 1
                    return
                if k == len(self.books) - 1:
                    return -1
        else:
            return -2

    def update_book(self, title, author, genre):
        for book in self.books:
            if book["title"] == title:
                book["author"] = author
                book["genre"] = genre

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("670x500")

        self.library = Library()

        # Creating the entry fields
        self.id_entry = tk.Entry(root, width=30)
        self.title_entry = tk.Entry(root, width=30)
        self.author_entry = tk.Entry(root, width=30)
        self.genre_entry = tk.Entry(root, width=30)

        # Creating the buttons
        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.remove_button = tk.Button(root, text="Remove Book", command=self.remove_book)
        self.update_button = tk.Button(root, text="Update Book", command=self.update_book)
        self.display_button = tk.Button(root, text="Display Books", command=self.display_books)

        # Adjusting the entry fields' positions
        self.id_entry.grid(row=4, column=2, columnspan=2, padx=10, pady=5)
        self.title_entry.grid(row=5, column=2, columnspan=2, padx=10, pady=5)
        self.author_entry.grid(row=6, column=2, columnspan=2, padx=10, pady=5)
        self.genre_entry.grid(row=7, column=2, columnspan=2, padx=10, pady=5)
        
        # Creating the description
        tk.Label(root, text="Welcome to Leonard's library! Some of our favourites this month include 'To Kill a Mockingbird' by Harper Lee \n and 'A Little Life' by Hanya Yanagihara. We hope you enjoy your stay!").grid(row=0, column=0, columnspan=15, padx=10, pady=5, sticky=tk.W)
        tk.Label(root, text="To add or remove a book, please fill up the book's Title, Author, and Genre fields but keep the Unique ID field empty.").grid(row=1, column=0, columnspan=15, padx=10, pady=5, sticky=tk.W)
        tk.Label(root, text="To update a book's features, please fill up the book's Unique ID field, along with the new attributes. \n If there are no changes to a certain attribute, please leave it blank. \n").grid(row=2, column=0, columnspan=15, padx=10, pady=5, sticky=tk.W)

        # Creating the entry fields' titles and positions
        tk.Label(root, text="Unique ID:").grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
        tk.Label(root, text="Title:").grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
        tk.Label(root, text="Author:").grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)
        tk.Label(root, text="Genre:").grid(row=7, column=1, padx=10, pady=5, sticky=tk.W)

        # Adjusting the buttons' positions
        self.add_button.grid(row=11, column=1, padx=0, pady=10)
        self.remove_button.grid(row=11, column=2, padx=0, pady=10)
        self.update_button.grid(row=11, column=3, padx=0, pady=10)
        self.display_button.grid(row=11, column=4, padx=0, pady=10)
        
    def clean_input(self, string):
        while string[0] == " ":
            string = string[1:]
        while string[-1] == " ":
            length = len(string)
            string = string[:length - 1]
        return string

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        
        title = self.clean_input(title)
        author = self.clean_input(author)
        genre = self.clean_input(genre)

        if title and author and genre:
            self.library.add_book(title, author, genre)
            messagebox.showinfo("Success", f'Book "{title}" added to the library.')
        else:
            messagebox.showwarning("Warning", "Please enter all book details.")

    def remove_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        
        title = self.clean_input(title)
        author = self.clean_input(author)
        genre = self.clean_input(genre)

        if title and author and genre:
            result = self.library.remove_book(title, author, genre)
            if result == -1:
                messagebox.showwarning("Warning", "No matching book exists. Please enter the correct title, author, and genre of the book to remove.")
            elif result == -2:
                messagebox.showwarning("Warning", "The library is empty.")
            else:
                messagebox.showinfo("Success", f'Book "{title}" removed from the library.')
        else:
            messagebox.showwarning("Warning", "Please enter the title, author, and genre of the book to remove.")

    def update_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        
        title = self.clean_input(title)
        author = self.clean_input(author)
        genre = self.clean_input(genre)

        if title and author and genre:
            self.library.update_book(title, author, genre)
            messagebox.showinfo("Success", f'Book "{title}" updated.')
        else:
            messagebox.showwarning("Warning", "Please enter the title of the book to update.")

    def display_books(self):
        self.destroy_widgets(root)
        if self.library.books:
            count = 0
            for book in self.library.books:
                tk.Label(root, text=f'Title: {book["title"]}, Author: {book["author"]}, Genre: {book["genre"]}, Count: {book["count"]}').grid(row=12 + count, column=1, columnspan=3, padx=0, pady=10, sticky=tk.W)
                count += 1
        else:
            messagebox.showwarning("Warning", "The library is empty.")
            
    def destroy_widgets(self, root):
        # Get all widgets in the grid
        widgets = root.grid_slaves()

        # Destroy widgets below row 4
        for widget in widgets:
            widget_row = widget.grid_info()["row"]
            if widget_row > 11:
                widget.grid_forget()
                
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()
