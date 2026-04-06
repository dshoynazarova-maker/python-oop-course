def track_change(func):
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        print(f'[STOCK] {value}')
        return value
    return wrapper
        
class Ingredient:
    _all_ingredients = []
    def __init__(self, name, cost_per_unit, units):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.units = units

        self._all_ingredients.append(self)

    @track_change
    def order(self, amount):
        self.amount = amount

        self.units += amount
        return f'{self.name}: ordered {self.amount}, now {self.units}'
    
    @track_change
    def use(self, amount):
        if amount > self.units:
            return f'Not enough {self.name} in kitchen'
        else:
            self.units -= amount
            return f'{self.name}: used {amount}, now {self.units}'
        
    def total_cost(self):
        return round((self.cost_per_unit * self.units),2)
    
    @classmethod
    def from_order_form(cls, entry):
        cls.entry = entry
        name , cost, units = entry.split(':')
        return cls(name, float(cost), int(units))
    
    @staticmethod
    def is_valid_code(code):
        strr, numm = code.split('-')
        if strr == 'ING' and numm.isdigit:
            return True
        else:
            return False
        
    @classmethod
    def kitchen_value(cls):
        #_all_ingredients [obj1{name,cost,units},obj2,obj3]
        #total_cost(obj1.cost)
        final = []
        total = 0
        for costs in cls._all_ingredients:
            result = cls.total_cost(costs)
            final.append(result)

        for cost in final:
            total += cost
        return round(total,2)
    #sum(cls.total_cost(costs.cost_per_unit))



i1 = Ingredient("Rice", 3.20, 60)
i2 = Ingredient.from_order_form("Olive Oil:15.75:8")

i1.order(15)
i1.use(50)
i1.use(100)
i2.use(3)

print(f"{i1.name}: cost = ${i1.total_cost()}")
print(f"{i2.name}: cost = ${i2.total_cost()}")

print(f"Valid code 'ING-012': {Ingredient.is_valid_code('ING-012')}")
print(f"Valid code 'FD-999': {Ingredient.is_valid_code('FD-999')}")
print(f"Kitchen total: ${Ingredient.kitchen_value()}")



    
        


    
    
    
    
    
