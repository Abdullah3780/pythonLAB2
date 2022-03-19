# Create a class BOOK with properties ISBN, Title, Price, Main Area
# , Sub Area, No of Pages. Constructor initialize these properties
# and show function display properties of and object. Call
# functions using object
class BOOK:
    ISBN = ''
    Title = ''
    Price = 0
    MainArea = ''
    SubArea = ''
    NoOfPages = 0

    def __init__(self, ISBN, Title, Price, MainArea, SubArea, NoOfPages):
        self.ISBN = ISBN
        self.Title = Title
        self.Price = Price
        self.MainArea = MainArea
        self.SubArea = SubArea
        self.NoOfPages = NoOfPages

    def ShowData(self):
        print('ISBN ', self.ISBN)
        print('Title ', self.Title)
        print('Price ', self.Price)
        print('MainArea ', self.MainArea)
        print('SubArea ', self.SubArea)


book1 = BOOK('QURAN', 'MAN', 200, 'KINDNESS', 'KAHAF', 1200)
book1.ShowData()
