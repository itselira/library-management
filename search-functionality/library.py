from book import Book
from user import User

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []
        
    def add_book(self, book):
        self.books.append(book)
    
    def add_user(self, user):
        self.users.append(user)
    
    def search_by_title(self, title):
        """Search for books by title (case-insensitive, partial match)"""
        title = title.lower()
        results = [book for book in self.books if title in book.title.lower()]
        return results
        
    def __str__(self):
        return f"{self.name} Library with {len(self.books)} books and {len(self.users)} users"
