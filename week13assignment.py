from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self,reader):
        self.reader = reader

    @abstractmethod
    def loan_days(self):
        pass

class Novel(Book):
    def loan_days(self):
        return 14
    
class Textbook(Book):
    def loan_days(self):
        return 30
    
class Magazine(Book):
    def loan_days(self):
        return 7
    
class LoanManager:
    def __init__(self):
        self.loans = []   # list of (reader, kind)

    def add(self, book:Book):
        self.loans.append(book)

    def run(self, slip, reminder):
        slip.print_slip(self.loans)
        reminder.send(self.loans)

class Slip(ABC):
    @abstractmethod
    def print_slip(self,loans):
        pass

class PaperSlip(Slip):
    def print_slip(self,loans):
        for book in loans:
            reader = book.reader
            days = book.loan_days()
            print(f'{reader} -> {days} days')

class Reminder(ABC):
    @abstractmethod
    def send(self,loans):
        pass

class TelegramReminder(Reminder):
    def send(self,loans):
        for book in loans:
            reader = book.reader
            days = book.loan_days()
            print(f'[TG → {reader}] Return in {days} days')

library = LoanManager()
library.add(Novel("Tony"))
library.add(Textbook("Steve"))
library.add(Magazine("Thor"))

library.run(PaperSlip(), TelegramReminder())


    
    
    
    

