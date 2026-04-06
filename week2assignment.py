class HotelFloor:
    def __init__(self,name,total_rooms,occupied_rooms = 0):
        self._name = name
        self.total_rooms = total_rooms
        self.occupied_rooms = occupied_rooms
    
    @property
    def name(self):
        return self._name
    @property
    def total_rooms(self):
        return self._total_rooms
    @total_rooms.setter
    def total_rooms(self, value):
        if value < 1:
            raise ValueError("Total rooms must be at least 1")
        self._total_rooms = value
    @property
    def occupied_rooms(self):
        return self._occupied_rooms
    @occupied_rooms.setter
    def occupied_rooms(self, value):
        if value < 0:
            raise ValueError("Occupied rooms cannot be negative")
        if value > self.total_rooms:
            raise ValueError("Occupied rooms cannot exceed total rooms")
        self._occupied_rooms = value
    @property
    def vacant_rooms(self):
        return self.total_rooms - self.occupied_rooms
    @property
    def occupancy_rate(self):
         return round((self.occupied_rooms / self.total_rooms) * 100, 1)
    def check_in(self,rooms):
        if rooms <= 0:
            raise ValueError('Number of rooms must be positive')
        if rooms > self.vacant_rooms:
            raise ValueError('Not enough vacant rooms')
        self.occupied_rooms += rooms
    def check_out(self,rooms):
        if rooms <= 0:
            raise ValueError('Number of rooms must be positive')
        if rooms > self.occupied_rooms:
            raise ValueError('Cannot check out more than occupied')
        self.occupied_rooms -= rooms
        
f = HotelFloor("Floor 3", 40)
print(f.name, f.vacant_rooms, f.occupancy_rate)

f.check_in(25)
print(f.occupied_rooms, f.occupancy_rate)

f.check_out(10)
print(f.vacant_rooms)

try:
    f.check_in(30)
except ValueError as e:
    print(e)

try:
    f.name = "X"
except AttributeError:
    print("Cannot change floor name")




    

    
