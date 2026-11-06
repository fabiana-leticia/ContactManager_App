# Hash Table, efficient storage structure
#average 0(1) time for add, search and delete

class HashTable:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        #convert name to index number within table size
        return hash(key) % self.capacity

    def insert(self, key, value):
        #add contact, return false if name already exists
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return False  #duplicate found
        self.table[index].append((key, value))
        return True

    def get(self, key):
        #find contact by name, return none if not found
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
            return None

    def delete(self, key):
        #remove contact by name
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return True
        return False

    def get_all(self):
        #return all contacts as a single list
        result = []
        for bucket in self.table:
            for _, contact in bucket:
                result.append(contact)
        return result