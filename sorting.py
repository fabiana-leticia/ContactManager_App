#bubble sort, orders contacts alphabetically 

def bubble_sort_contacts(contacts_list):
    n = len(contacts_list)
    for i in range(n):
        swapped = False #early exit flag
        for j in range(0, n - i - 1):
            if contacts_list[j].name > contacts_list[j + 1].name:
                #swap positions if in wrong order
                contacts_list[j], contacts_list[j + 1] = contacts_list[j +1], contacts_list[j]
                swapped = True
        if not swapped:
            break #already sorted, stop early
    return contacts_list