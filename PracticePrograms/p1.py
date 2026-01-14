
class Queue:

    def __init__(self):
        self.stack = []
   
    def add_book(self,num):
        self.stack.append(num)

    def remove_book(self):
        print(f"remove the book: {self.stack[0]}")
        self.stack.remove(self.stack[0])
          
    def get_queue(self):
        print(f"All the books: {self.stack}")
 
fiction_books = Queue()
fiction_books.add_book("Harry potter")
fiction_books.add_book("snow white")
fiction_books.add_book("Narnia")
fiction_books.add_book("Charlie chocolate factory")
fiction_books.get_queue()
fiction_books.remove_book()
fiction_books.get_queue()
fiction_books.remove_book()
fiction_books.get_queue()

# stack or queue

class Stack:

    def __init__(self):
        self.stack = []
   
    def add_book(self,num):
        self.stack.append(num)

    def remove_book(self):
        book =  self.stack.pop()
        print(f"remove the book: {book}")
    
    def get_stack(self):
        print(f"All the books: {self.stack}")
 
    
fiction_books = Stack()
fiction_books.add_book("Harry potter")
fiction_books.add_book("snow white")
fiction_books.add_book("Narnia")
fiction_books.add_book("Charlie chocolate factory")
fiction_books.get_stack()
fiction_books.remove_book()
fiction_books.get_stack()
