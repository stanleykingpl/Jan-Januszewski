import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False



def setup():
    size(220,100)
    global library, Madzia, Jan
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Pan Samochodzik"]
    library = Library(books) 
    Madzia = Customer()
    Jan = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
            library.lendBook(Jan.requestBook("Pan Samochodzik")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.addBook(Jan.returnBook())
            
class ZadanieDziesiate(unittest.TestCase):

    def test_JJ_2(self): # nazwy testów powinny się zaczynać od test
        Jan = Customer() # testy powinny być od siebie niezależne, a więc i obiekty zdefiniowane wewnątrz
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)  # klasa biblioteki nie należy do klasy testó, więc używanie self jest tu błędem
        library.lendBook(Jan.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], library.availableBooks)
        self.assertEqual(Jan.book, "Harry Potter")
        self.assertTrue(Jan.haveBook)

    def test_JJ_3(self):
        Jan = Customer()
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books) 
        library.addBook("2012")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Harry Potter", "2012"], library.availableBooks)
        
if __name__ == '__main__':
    unittest.main()
    
#1,5pkt
