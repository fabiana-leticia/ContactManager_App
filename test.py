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