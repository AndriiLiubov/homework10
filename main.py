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
        if not self.validate_phone(value):
            raise ValueError("Wrong phone number format")
        self.value = value

    def validate_phone(self, value):    
        return isinstance(value, str) and len(value) == 10 and value.isdigit()
            

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                return phone
        raise ValueError(f'this phone is not exist in {self.name.value}')

    def edit_phone(self, old_phone, new_phone ):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                return i


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
                raise KeyError("Already exists")
        self.data[record.name.value] = record

    def find(self, record):
        for key, value in self.data.items():
            if key == record:
                return value

    def delete(self, record):
        if record in self.data:
            self.data.pop(record)


