#compare sorting.py
#quick test - bubble sort vs merge sort
#just to see how much faster one is with more data

import time 
from contact import Contact
from sorting import bubble_sort
from faker import Faker

fake = Faker()

def generate_contacts(count):
    """Create a list of random contacts"""
    contacts = []
    for _ in range(count):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        contacts.append(Contact(name,phone,email))
    return contacts

def measure_time(contact_list, sort_function):
    """measure how long a sorting function takes to run"""
    copy_list = contact_list.copy()
    start = time.time()
    sort_function(copy_list)
    end = time.time()
    return end - start

# simple merge sort implementation for comparison

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)