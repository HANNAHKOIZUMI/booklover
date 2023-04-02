import pandas as pd

class BookLover():

    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name': [], 'book_rating': []})
        
    def add_book(self, book_name, rating):
        self.book_name = book_name
        self.rating = rating
        if book_name in set(self.book_list['book_name']):
            print("Book is already on list.")
        else:
            new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
            
    def has_read(self,book_name):
        if book_name in set(self.book_list['book_name']):
            return True
        else:
            return False
    
    def num_books_read(self):
        num_books = self.num_books
        print(num_books)
        return num_books
        
    def fav_books(self):
        fav_books = self.book_list[self.book_list["book_rating"] > 3]
        if fav_books.empty:
            return "You have none"
        else:
            return fav_books