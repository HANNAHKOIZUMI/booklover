import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        print(student.book_list)
        
        expected = ("Doom Loop")
        self.assertEqual(student.book_name,expected)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        student.add_book("Doom Loop", 2)
        if (student.book_list['book_name']=='Doom Loop').sum() != 1:
            raise AssertionError('Book already exists in book list.')
    
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        actual = student.has_read("Doom Loop")
        message = "The reader has not read this book."
        self.assertTrue(actual, message) 
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        actual = student.has_read("Cat in the Hat")
        message = "Test value is not false."
        self.assertFalse(actual, message) 
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        student.add_book("Little Women", 4)
        student.add_book("Ender's Game", 3)
        expected = 3
        actual = student.num_books_read()
        self.assertEqual(actual, expected)

    def test_6_fav_books(self): 
        student = BookLover("Hannah", "hk@gmail.com", "Nonfiction")
        student.add_book("Doom Loop", 2)
        student.add_book("Little Women", 4)
        student.add_book("Ender's Game", 3)
        fav_books = student.fav_books() 
        self.assertTrue(all(fav_books["book_rating"] > 3))
    
if __name__ == '__main__':
    unittest.main(verbosity=3)

    