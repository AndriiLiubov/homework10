from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self.validate_phone()

    def validate_phone(self):    
        if not ((isinstance(self.value, str)) and len(self.value) == 10 and self.value.isdigit()):
            raise ValueError("Wrong phone number format")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == Phone(phone).value:
                self.phones.remove(i)

    def edit_phone(self, old_phone, new_phone ):
        for i in self.phones:
            if i.value == Phone(old_phone).value:
                i.value = Phone(new_phone).value
                return
           
        raise ValueError

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == Phone(phone).value:
                return i


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        for key in self.data:
            if key == record.name.value:
                raise KeyError("Already exists")
        self.data.update({record.name.value: record})

    def find(self, record):
        for key, value in self.data.items():
            if key == record:
                return value

    def delete(self, record):
        if record in self.data:
            self.data.pop(record)


