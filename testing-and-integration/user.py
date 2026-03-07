class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []
    
    def __str__(self):
        return f"User: {self.name} (ID: {self.user_id}) - Books borrowed: {len(self.books_borrowed)}"
    
    def return_all_books(self, library):
        books_to_return = self.books_borrowed.copy()
        return_count = 0
        
        for book in books_to_return:
            # Return each book
            book.available = True
            book.borrower = None
            self.books_borrowed.remove(book)
            return_count += 1
            
        return return_count
