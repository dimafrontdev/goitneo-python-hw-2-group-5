from collections import UserDict


class Field:
    # Базовий клас для зберігання даних поля.
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # Клас для зберігання імені контакту.
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    # Клас для номера телефону з перевіркою на 10 цифр.
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits")
        super().__init__(value)


class Record:
    # Клас для зберігання інформації про контакт (ім'я та телефони)
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Методи для додавання, редагування, видалення та пошуку телефонів.

    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == old_phone:
                self.phones[i] = Phone(new_phone)

    def remove_phone(self, del_phone):
        for i, p in enumerate(self.phones):
            if str(self.phones[i]) == del_phone:
                phone = self.phones[i]
                self.phones.remove(phone)

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"\033[94mContact name: \033[92m{self.name.value}, \033[94mphones: \033[92m{phones_str}\033[0m"


class AddressBook(UserDict):
    # Клас для управління адресною книгою (додавання, пошук, видалення записів).
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
