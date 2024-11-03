class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Title: {self.title}, Author: {self.author}, Year: {self.year}')
        
    @classmethod
    def from_dict(cls, book_dict):
        return cls(
            title=book_dict['title'],
            author=book_dict['author'],
            year=book_dict['year']
        )
           
assassins_apprentice = Book('Assassins Apprentice', 'Robin Hobb', 1995)
assassins_apprentice.display_info()

mistborn_dict = {
    'title': 'The Final Empire',
    'author': 'Brandon Sanderson',
    'year': 2006
}
mistborn = Book.from_dict(mistborn_dict)
mistborn.display_info()