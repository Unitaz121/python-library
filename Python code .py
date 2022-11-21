#student number F020717
import sys  #information about functions constants and methods of the Python interpreter.
import ast  # abstract syntax trees
import itertools    #iterator for efficient looping
from itertools import chain       

class Library:  

    def __init__(self, listofbooks):
        self.availablebooks = listofbooks  
        
    def displayAvailablebooks(self):    
        print("================================")       
        for index in sorted(self.availablebooks):    
            print(index + "," + "," .join(self.availablebooks[index]))            

    def deleteAllBooks(self):   
        self.availablebooks.clear()   
        print("All books have been desleted!")   
        main()  
    
    def addBook(self, returnedBook): #input for keyboard
        self.bookTitle = returnedBook[0]
        del returnedBook[0]
        self.availablebooks.update({self.bookTitle: returnedBook})  
        print("Book is added")     

    def returnBook(self): 
        print("Enter the title of the book")
        self.title = raw_input()

        while (self.title in self.availablebooks):    
            print("A book by this title already exists!")
            self.title = raw_input()
        
        print("Enter the author of the book")
        self.author = raw_input()
        print("Enter the year of the book")
        self.year = raw_input()
        print("Enter the page count of the book")   
        self.pageCount = raw_input()
        self.book = [self.title, self.author, self.year, self.pageCount]
        return self.book    
        
    def deleteOneBook(self):   
        print("Type a book title you want to remove")   
        bookTitleInput = raw_input()  
        self.bookDeleteResponse = self.availablebooks.pop(bookTitleInput, None) 
        if self.bookDeleteResponse == None: 
            print(bookTitleInput + " does not exist!")  
        else:   
            print(bookTitleInput + " has been deleted")         
        self.displayAvailablebooks()        
      
def main(): #function 
    library = Library({})  
    done = False    
    while done == False:    
        print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Add a book
                  3. Menu   
                  4. Exit   
                  """)  
        choice = int(input("Enter Choice:"))   #if conditions                              
        if choice == 1: 
            library.displayAvailablebooks() #shows the output on the screen 
        elif choice == 2:
            library.addBook(library.returnBook())  
        elif choice == 3:  # sub menu 
            print(""" ======ACTIONS MENU======= 
                              1. Remove        
                              2. Main Menu 
                              """)  
            choice = int(input("Enter Choice:"))        
            if choice == 1: 
                library.displayAvailablebooks()  
                print(""" ======REMOVE======= 
                                                1. Remove one book        
                                                2. Remove all books 
                                                3. Main Menu               
                                                """)
                choice = int(str(input("Enter Choice:")))     
                if choice == 1: 
                    library.deleteOneBook()  

                elif choice == 2:       
                    print("""Are you sure you want to remove all books?
                                                      1. Yes
                                                      2. No  
                                                      """)  
                    choice = int(input("Enter Choice:"))    
                    if choice == 1:  
                        library.deleteAllBooks()    
                    elif choice == 2:    
                        library.displayAvailablebooks() 
                        main()    
                    elif choice == 3:   
                        main()  
                elif choice == 2:   
                        main()  
                     
            if choice == 2:  
                library.displayAvailablebooks()  
            else:   
                library.displayAvailablebooks()   
                print("Please choose from a list")  
        elif choice == 4:   
            sys.exit("""Good Bye!
                        Preass Arrow Up and Enter to a library    
                        """)      
        else:   
            library.displayAvailablebooks() 
            print("Please choose from a list")  
            
main()  
