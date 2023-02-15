from faker import Faker
import random

fake = Faker()

class BaseContact:
    def __init__(self, name, surname, phone_number, email):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email

    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname)


class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone_number, email, position, company_name, work_phone_number):
        super().__init__(name, surname, phone_number, email)
        self.position = position
        self.company_name = company_name
        self.work_phone_number = work_phone_number

    def contact(self):
        print(f"Wybieram numer {self.work_phone_number} i dzwonię do {self.name} {self.surname}")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + len(self.position) + len(self.company_name)


def create_contacts(contact_type, num_contacts):
    contacts = []
    for i in range(num_contacts):
        name = fake.first_name()
        surname = fake.last_name()
        phone_number = fake.phone_number()
        email = fake.email()
        if contact_type == "business":
            position = fake.job()
            company_name = fake.company()
            work_phone_number = fake.phone_number()
            contact = BusinessContact(name, surname, phone_number, email, position, company_name, work_phone_number)
        else:
            contact = BaseContact(name, surname, phone_number, email)
        contacts.append(contact)
    return contacts
