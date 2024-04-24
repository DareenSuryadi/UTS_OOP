class User:
    """Abstract class representing a system user."""

    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password

    def login(self):
        pass

    def logout(self):
        pass


class Member(User):
    """Class representing a library member."""

    def __init__(self, user_id, username, password, name, email):
        super().__init__(user_id, username, password)
        self.name = name
        self.email = email
        self.borrowed_books = []

    def search_book(self, library, title, author):
        """Searches for a book in the library."""
        return library.search_book(title, author)

    def borrow_book(self, book):
        """Borrows a book."""
        self.borrowed_books.append(book)

    def return_book(self, book):
        """Returns a borrowed book."""
        self.borrowed_books.remove(book)


class Librarian(User):
    """Class representing a library staff member."""

    def __init__(self, user_id, username, password):
        super().__init__(user_id, username, password)

    def add_book(self, library, book):
        """Adds a new book to the library system."""
        library.add_book(book)
        library.update_search_index(book)

    def update_book(self, library, book):
        """Updates details of an existing book."""
        pass

    def delete_book(self, library, book):
        """Removes a book from the library system."""
        pass

    def manage_member(self, library, member):
        """Manages member information (details to be implemented)."""
        pass

    def add_new_book(self, library, title, author):
        """Allows librarian to add a new book to the library system."""
        new_book = Book(title, author)
        self.add_book(library, new_book)
        print(f"New book added: {new_book.get_book_info()}")

    def search_books_by_author(self, library, author):
        """Searches for books by a specific author."""
        found_books = library.search_books_by_author(author)
        if found_books:
            print(f"Books found by {author}:")
            for book in found_books:
                print(book.get_book_info())
        else:
            print(f"No books found by {author}")


class Book:
    """Class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_book_info(self):
        """Returns information about the book."""
        return f"Title: {self.title}, Author: {self.author}"


class Library:
    """Class representing the library system."""

    def __init__(self):
        self.books = []
        self.members = []
        self.search_index = {}

    def authenticate_user(self, username, password):
        pass

    def search_book(self, title, author):
        """Searches for a book by title or author."""
        if title.lower() in self.search_index:
            return self.search_index[title.lower()]
        if author:
            found_books_by_author = [book for book in self.books if book.author.lower() == author.lower()]
            if found_books_by_author:
                return found_books_by_author
        return None

    def search_books_by_author(self, author):
        """Searches for books by a specific author."""
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def add_book(self, book):
        """Adds a new book to the library collection."""
        self.books.append(book)

    def update_search_index(self, book):
        """Update search index with the new book."""
        self.search_index[book.title.lower()] = book

    def update_book(self, book):
        pass

    def borrow_book(self, member, book_title):
        """Allows a member to borrow a book."""
        book = self.search_book(book_title, None)
        if book:
            if isinstance(book, list):
                book = book[0]
            if book in self.books:
                self.books.remove(book) 
                member.borrow_book(book)  
                print(f"Book '{book.title}' borrowed by {member.name}")
            else:
                print(f"Book '{book.title}' is currently unavailable")
        else:
            print(f"Book with title '{book_title}' not found in the library")

    def return_book(self, member, book_title):
        """Allows a member to return a borrowed book."""
        borrowed_books = member.borrowed_books
        for borrowed_book in borrowed_books:
            if borrowed_book.title.lower() == book_title.lower():
                self.books.append(borrowed_book)   
                member.return_book(borrowed_book)  
                print(f"Book '{borrowed_book.title}' returned by {member.name}")
                return
        print(f"Book with title '{book_title}' not found in the borrowed books of {member.name}")


library = Library()

book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = Book("The Lord of the Rings", "J.R.R. Tolkien")
book3 = Book("Harry Potter 1", "J.K. Rowling")
book4 = Book("Harry Potter 2", "J.K. Rowling")
book5 = Book("The Lord of the Rings II", "J.R.R. Tolkien")


librarian = Librarian(1, "librarian_username", "librarian_password")

librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_book(library, book3)
librarian.add_book(library, book4)
librarian.add_book(library, book5)


member = Member(2, "member_username", "member_password", "John Doe", "john.doe@email.com")

search_title = "The Lord of the Rings"

found_book = member.search_book(library, search_title, None)

if found_book:
    if isinstance(found_book, list):
        for book in found_book:
            print(f"Book found: {book.get_book_info()}")
    else:
        print(f"Book found: {found_book.get_book_info()}")
else:
    print(f"No book found with title: {search_title}")

librarian.add_new_book(library, "Harry Potter and the Philosopher's Stone", "J.K. Rowling")

search_title_new = "Harry Potter and the Philosopher's Stone"
found_book_new = member.search_book(library, search_title_new, None)

if found_book_new:
    if isinstance(found_book_new, list):
        for book in found_book_new:
            print(f"Book found: {book.get_book_info()}")
    else:
        print(f"Book found: {found_book_new.get_book_info()}")
else:
    print(f"No book found with title: {search_title_new}")

library.borrow_book(member, "Harry Potter and the Philosopher's Stone")

library.return_book(member, "Harry Potter and the Philosopher's Stone")

author_to_search = "J.R.R. Tolkien"

found_books_by_author = library.search_books_by_author(author_to_search)

if found_books_by_author:
    print(f"Books written by {author_to_search}:")
    for book in found_books_by_author:
        print(book.get_book_info())
else:
    print(f"No books written by {author_to_search}")
