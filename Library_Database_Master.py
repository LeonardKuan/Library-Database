import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        if self.books:
            for k in range(len(self.books)):
                # If the book is already in the library
                if title == self.books[k]["title"] and author == self.books[k]["author"] and genre == self.books[k]["genre"]:
                    self.books[k]["count"] += 1
                    break
                # If the book is new, i.e. not in the library
                if k == len(self.books) - 1:
                    unique_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
                    self.books.append({"id": unique_id, "title": title, "author": author, "genre": genre, "count": 1})
        else:
            # If the library is empty, just add the book, which will be the first
            unique_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            self.books.append({"id": unique_id, "title": title, "author": author, "genre": genre, "count": 1})

    def remove_book(self, title, author, genre):
        if self.books:
            for k in range(len(self.books)):
                # If the book is already in the library
                if title == self.books[k]["title"] and author == self.books[k]["author"] and genre == self.books[k]["genre"]:
                    # If the book count is exactly 1, simply remove it from the library
                    if self.books[k]["count"] == 1:
                        del self.books[k]
                    # If the book count is > 1, reduce the count by 1
                    else:
                        self.books[k]["count"] -= 1
                    return
                # If no such book is found in the library, return an error code as you can't remove a non-existent book
                if k == len(self.books) - 1:
                    return -1
        # If the library is empty, return an error code as you can't remove a non-existent book
        else:
            return -2

    def update_book(self, unique_id, title, author, genre):
        if self.books:
            for k in range(len(self.books)):
                # If the book is in the library, update it
                if self.books[k]["id"] == unique_id:
                    self.books[k]["title"] = title
                    self.books[k]["author"] = author
                    self.books[k]["genre"] = genre
                    return
                # If no such book is found in the library, return an error as you can't update a non-existent book
                if k == len(self.books) - 1:
                    return -1
        # If the library is empty, return an error code as can't update a non-existent book
        else:
            return -2

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
    
        if title and author and genre:
            title = self.clean_input(title)
            author = self.clean_input(author)
            genre = self.clean_input(genre)
            
            self.library.add_book(title, author, genre)
            messagebox.showinfo("Success", f'Book "{title}" added to the library.')
        else:
            messagebox.showwarning("Warning", "Please enter all book details.")

    def remove_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()

        if title and author and genre:
            title = self.clean_input(title)
            author = self.clean_input(author)
            genre = self.clean_input(genre)
            
            result = self.library.remove_book(title, author, genre)
            
            # If no such book is found in the library
            if result == -1:
                messagebox.showwarning("Warning", "No matching book exists. Please enter the correct title, author, and genre of the book to remove.")
            # If the library is empty
            elif result == -2:
                messagebox.showwarning("Warning", "The library is empty.")
            # Successfully removed
            else:
                messagebox.showinfo("Success", f'Book "{title}" removed from the library.')
        else:
            messagebox.showwarning("Warning", "Please enter the title, author, and genre of the book to remove.")

    def update_book(self):
        unique_id = self.id_entry.get()
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        
        if unique_id and title and author and genre:
            unique_id = self.clean_input(unique_id)
            title = self.clean_input(title)
            author = self.clean_input(author)
            genre = self.clean_input(genre)

            result = self.library.update_book(unique_id, title, author, genre)
            
            # If no such book is found in the library
            if result == -1:
                messagebox.showwarning("Warning", "No matching book exists. Please enter the correct unique ID of the book to update.")
            # If the library is empty
            elif result == -2:
                messagebox.showwarning("Warning", "The library is empty.")
            # Successfully updated
            else:
                messagebox.showinfo("Success", f'Book "{title}" updated within the library.')
        else:
            messagebox.showwarning("Warning", "Please enter the unique ID of the book to be updated, followed by the new title, author, and genre.")

    def display_books(self):
        self.destroy_widgets(root)
        
        book_list = [["Unique ID", "Title", "Author", "Genre", "Quantity"]]
        if self.library.books:
            for k in range(len(self.library.books)):
                book_list.append([self.library.books[k]["id"], self.library.books[k]["title"], self.library.books[k]["author"], self.library.books[k]["genre"], self.library.books[k]["count"]])
             # i is # of rows
            for i in range(len(book_list)):
                # k is # of columns
                for k in range(5):
                    if i == 0:
                        self = Entry(root, width=20, fg='black', font=('Arial', 10, 'bold'))
                    else:
                        self = Entry(root, width=20, fg='black', font=('Arial', 10))
                    self.grid(row=i+12, column=k, columnspan=2)
                    self.insert(END, book_list[i][k])
        else:
            messagebox.showwarning("Warning", "The library is empty.")
        
    def destroy_widgets(self, root):
        # Get all widgets in the grid
        widgets = root.grid_slaves()

        # Destroy widgets below row 11
        for widget in widgets:
            widget_row = widget.grid_info()["row"]
            if widget_row > 11:
                widget.grid_forget()
                
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryGUI(root)
    root.mainloop()