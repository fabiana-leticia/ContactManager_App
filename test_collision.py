from hash_table import HashTable
ht = HashTable(capacity=1)
ht.insert("alice", "07700 900001")
ht.insert("bob", "07700 900002")
ht.insert("carol", "07700 900003")
 
print(ht.get("alice"))    # first in bucket
print(ht.get("bob"))      # second in bucket
print(ht.get("carol"))    # third in bucket
print(ht.get("dave"))     # not present

import unittest
from hash_table import HashTable
 
class TestHashTable(unittest.TestCase):
    def test_get_with_collisions(self):
        ht = HashTable(capacity=1)
        ht.insert("alice", 1)
        ht.insert("bob", 2)
        self.assertEqual(ht.get("bob"), 2)
        self.assertIsNone(ht.get("dave"))
 
if __name__ == "__main__":
     unittest.main()
