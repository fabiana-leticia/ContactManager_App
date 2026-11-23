# test.py — Bubble Sort vs Merge Sort Performance Test

import time
from contact import Contact
from sorting import bubble_sort_contacts
from faker import Faker

fake = Faker()


def generate_contacts(count):
    contacts = []
    for _ in range(count):
        name = fake.name()
        phone = fake.phone_number()
        email = fake.email()
        contacts.append(Contact(name, phone, email))
    return contacts


def measure_time(contact_list, sort_function):
    copy_list = contact_list.copy()
    start = time.time()
    sort_function(copy_list)
    end = time.time()
    return end - start


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


# START THE TEST — this runs everything
if __name__ == "__main__":
    print("=" * 60)
    print("📊 Bubble Sort vs Merge Sort — Speed Comparison")
    print("=" * 60)
    print()
    
    sizes = [100, 500, 1000, 2000]
    
    for size in sizes:
        print(f"--- Testing with {size} contacts ---")
        test_data = generate_contacts(size)
        
        bubble_time = measure_time(test_data, bubble_sort_contacts)
        merge_time = measure_time(test_data, merge_sort)
        
        print(f"   Bubble Sort:  {bubble_time:.6f} seconds")
        print(f"   Merge Sort:   {merge_time:.6f} seconds")
        if merge_time > 0:
            print(f"   → Merge Sort is {bubble_time / merge_time:.1f}x faster")
        print()
    
    print("=" * 60)
    print("✅ Test Complete")
    print("=" * 60)
