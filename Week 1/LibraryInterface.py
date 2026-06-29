from abc import ABC, abstractmethod

class LibraryUser (ABC):
    @abstractmethod
    def registerAccount(LibraryUser):
        pass

    @abstractmethod
    def requestBook(LibraryUser):
        pass

class KidUsers (LibraryUser):
    def __init__(self, age, bookType):
        self.age = age 
        self.bookType = bookType
    
    def registerAccount(self):

        if self.age < 12:
            print("You have successfully registered under a Kids Account")
        else:
            print("Sorry, Age must be less than 12 to register as a kid")
        
    def requestBook(self):
        if self.bookType == "Kids":
            print("Book Issued successfully, please return the book within 10 days")

        else:
            print("Oops, you are allowed to take only kids books")
    
class AdultUser(LibraryUser):
    def __init__(self, age, bookType):
        self.age = age 
        self.bookType = bookType
    
    def registerAccount(self):

        if self.age > 12:
            print("You have successfully registered under an Adult Account")
        else:
            print("Sorry, Age must be greater than 12 to register as an adult")
        
    def requestBook(self):
        if self.bookType == "Fiction":
            print( "Book Issued successfully, please return the book within 10 days")

        else:
            print("Oops, you are allowed to take only Adult books")
    
Kid1 = KidUsers(10, "Kids")
Kid1.registerAccount()
Kid1.requestBook()

Kid2 = KidUsers(18, "fiction")
Kid2.registerAccount()
Kid2.requestBook()

Adult1 = AdultUser(5, "Kids")
Adult1.registerAccount()
Adult1.requestBook()

Adult2 = AdultUser(23, "Fiction")
Adult2.registerAccount()
Adult2.requestBook()
        