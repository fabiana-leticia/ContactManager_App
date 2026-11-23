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

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # run tests!

    if __name__=="__main__":
        print("=" * 60)
        print("📊 Bubble Sort vs Merge Sort — Speed Comparison")
        print("=" * 60)
        print()

        sizes = [100, 500, 1000,2000]

        for size in sizes:
            print(f"--- Testing with {size} contacts ---")
            test_data = generate_contacts(size)

            bubble_time = measure_time(test_data, bubble_sort)
            merge_time = measure_time(test_data, merge_sort)

            print(f"   Bubble Sort:  {bubble_time:.6f} seconds")
            print(f"   Merge Sort:   {merge_time:.6} seconds")
            if merge_time > 0:
                print(f"     - Merge Sort is {bubble_time / merge_time:.1}x faster!")
            print()

        print("=" * 60)
        print("Conclusion: More data = bigger advantage for Merge Sort")
        print("Bubble Sort = O(n^2). |  Merge Sort = O(n log n)")
        print("=" * 60)