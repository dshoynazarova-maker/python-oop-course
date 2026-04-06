class LibraryMember:
    library_name = 'City Library'
    total_members = 0
    def __init__(self,name, member_id, borrowed = None ):
        self.name = name
        self.member_id = member_id
        self.borrowed = []
        LibraryMember.total_members += 1
    def borrow_book(self,title):
        if title != '':
            self.borrowed.append(title)
            print(f'Borrowed: {title}')
    def return_book(self,title):
        if title in self.borrowed:
            self.borrowed.remove(title)
            print(f'Returned: {title}')
        else:
            print('Book not found')
    def display_member(self):
        print(f'Member: {self.name} ({self.member_id}) at {self.library_name}')

member1 = LibraryMember('Aziza','L-101') 
member2 = LibraryMember('Bekzod','L-102')  

member1.display_member()
member1.borrow_book('1984')
member1.borrow_book('Dune')
member1.return_book('Dune')

member2.display_member()
member2.return_book('Foundation')


print(f'Total members: {LibraryMember.total_members}')


