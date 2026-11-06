from contact import Contact
from hash_table import HashTable
from sorting import bubble_sort_contacts

class ContactManager:
    """Manages all contacts: add, search, delete, list"""

    def __init__(self):
        self.contacts_store = HashTable()

    def add_contact(self, name, phone, email):
        """Add a new contact. Returns True if added, False if name already exists"""
        new_contact = Contact(name, phone, email)
        return self.contacts_store.insert(name, new_contact)

    def search_contact(self, name):
        """Find contact by name. Returns contact object or none"""
        return self.contacts_store.get(name)

    def delete_contact(self, name):
        """Remove contact by name. Returns True if deleted"""
        return self.contacts_store.delete(name)

    def list_all_contacts(self):
        """Return all contacts sorted alphabetically by name"""
        raw_list = self.contacts_store.get_all()
        contacts_only = [item[1] for item in raw_list]
        return bubble_sort_contacts(contacts_only)