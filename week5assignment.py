from abc import ABC, abstractmethod

class Filter(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def apply(self,value):
        pass

    def check(self,value):
        result = self.apply(value)
        status = "PASS" if result else "FAIL"
        print(f'[{status}] {self.name}: {value}')
        return result

class ExtensionFilter(Filter):
    def __init__(self,allowed):
        self.allowed = allowed
        name = f'Extension({self.allowed})'
        super().__init__(name)

    def apply(self,value):
        result = False

        if value.endswith(".jpg"):
            result = True
        if value.endswith(".png"):
            result = True
        if value.endswith(".pdf"):
            result = True

        return result

class MaxSizeFilter(Filter):
    def __init__(self,max_size):
        self.max_size = max_size
        name = f'MaxSize({max_size})'
        super().__init__(name)

    def apply(self,value):
        return len(value) <= self.max_size

class NoSpacesFilter(Filter):
    def __init__(self):
        super().__init__('NoSpaces')

    def apply(self,value):   
        return ' ' not in value

class StartsWithLetterFilter:
    def __init__(self):
        self.name = "StartsWithLetter"

    def apply(self, value):
        if value != "":
            first = value[0]
            if ('a' <= first <= 'z') or ('A' <= first <= 'Z'):
                result = True
            else:
                result = False
        else:
            result = False

        return result

    def check(self, value):
        result = self.apply(value)
        status = "PASS" if result else "FAIL"
        print(f'[{status}] {self.name}: {value}')
        return result

class UploadReport:
    def __init__(self):
        self.entries = []

    def add(self, filter_name, value, passed):
        tupple = (filter_name, value, passed)
        self.entries.append(tupple)
        return tupple

    def summary(self):

        total = len(self.entries)
        passed = sum(1 for entry in self.entries if entry[2])
        failed = total - passed
        print(f'Total: {total}, Passed: {passed}, Failed: {failed}')
        result = (total, passed, failed)
        return result

class UploadField:
    def __init__(self, field_name):
        self.field_name = field_name
        self.filters = []
        self.report = UploadReport()


    def add_filter(self, filter_obj):
        return self.filters.append(filter_obj)
        
    def validate(self, value):
        print(f'Validating {self.field_name}: "{value}"')
        all_passed = True

        
        for checking in self.filters:
            outcome = checking.check(value)
            self.report.add(checking.name, value, outcome)
            if not outcome:
                all_passed = True
        outcome = all_passed
        return outcome

    def show_report(self):
        print(f"--- Report for {self.field_name} ---")
        return self.report.summary()
        
upload = UploadField('avatar')
upload.add_filter(ExtensionFilter(['jpg', 'png', 'pdf']))
upload.add_filter(MaxSizeFilter(20))
upload.add_filter(NoSpacesFilter())
upload.add_filter(StartsWithLetterFilter())

valid1 = upload.validate('profile_pic.jpg')
print(f'Valid: {valid1}')
print()

valid2 = upload.validate('my document.exe')
print(f'Valid: {valid2}')
print()

valid3 = upload.validate('123.png')
print(f'Valid: {valid3}')
print()

upload.show_report()

try:
    f = Filter('test')
except TypeError:
    print('Cannot instantiate abstract class')





            

        

        


        



    
    
    
    

        
    
    
