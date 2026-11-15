#create a class for a library that can hold books and allow users to borrow and return them
class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, title, author):
        if title not in self.books:
            self.books[title] = author
    def borrow_book(self, title, user):
        book1=(self.books.get(title))
        if book1:
            print(f'Book "harry potter" by jk rowling is available.')
        else:
            print(f'Book "harry potter" is not available.')
def borrow_book(self, title, user):
        book2=(self.books.get(title))
        if book2:
            print(f'Book "captin underpants" by david pilky is available.')
        else:
            print(f'Book "captin underpants" is not available.')
            def borrow_book(self, title, user):
                    book3=(self.books.get(title))
                    if book3:
                        print(f'Book "dog man" by david pilky is available.')
                    else:
                        print(f'Book "dog man" is not available.')
                        def borrow_book(self, title, user):
                                book4=(self.books.get(title))
                                if book4:
                                    print(f'Book "superman" by dc is available.')
                                else:
                                    print(f'Book "superman" is not available.')
                        
            
