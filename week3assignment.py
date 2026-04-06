class TicketBooking:
    def __init__(self, event_name: str, ticket_price: float, seat_count: int):
        self.event_name = event_name
        self.ticket_price = ticket_price
        self.seat_count = seat_count

    def __str__(self):
        return f'{self.event_name}: {self.seat_count} seat(s) at ${self.ticket_price}'
    
    def __repr__(self):
        return f'TicketBooking("{self.event_name}", {self.ticket_price}, {self.seat_count})'
    
    def __add__(self, booking):
        if isinstance(booking,TicketBooking) and self.event_name == booking.event_name:
            return TicketBooking(self.event_name, self.ticket_price,self.seat_count + booking.seat_count )
        elif isinstance(booking,int):
            return TicketBooking(self.event_name, self.ticket_price, self.seat_count+booking)
        else:
            return NotImplemented
        
    def __eq__(self,value):
        if isinstance(value,TicketBooking):
            return self.event_name == value.event_name and self.ticket_price == self.ticket_price
        else:
            return NotImplemented
        
    def __bool__(self):
        return self.seat_count > 0
    
booking1 = TicketBooking("Concert", 50.0, 4)
booking2 = TicketBooking("Concert", 50.0, 2)
booking3 = TicketBooking("Play", 30.0, 0)

print(str(booking1))
print(repr(booking1))
print(booking1 + booking2)
print(booking1 + 3)
print(booking1 == booking2)
print(bool(booking1))
print(bool(booking3))


    
        
