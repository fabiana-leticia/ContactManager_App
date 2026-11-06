#defines the contacts class, represents one person's details

class Contact:
    def __init__(self, name, phone, email):
        #runs automatically when creating a new contact
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        #clean format when printing
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"