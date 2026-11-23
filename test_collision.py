import unittest
from contact import Contact
from hash_table import HashTable

 
class TestHashTable(unittest.TestCase):
    def setUp(self):
    # runs before every test, so each test starts with a fresh table
     self.ht = HashTable()
     self.alice = Contact("Alice", "07700 900001", "alice@example.com")
     self.bob = Contact("Bob", "07700 900002", "bob@example.com")
     self.carol = Contact("Carol", "07700 900003", "carol@example.com")

    def test_get_with_collisions(self):
    # this is the test that catches the misplaced 'return None' bug
      ht = HashTable(capacity=1)
      ht.insert("Alice", self.alice)
      ht.insert("Bob", self.bob)
      ht.insert("Carol", self.carol)
      self.assertIs(ht.get("Alice"), self.alice)
      self.assertIs(ht.get("Bob"), self.bob)
      self.assertIs(ht.get("Carol"), self.carol)
      self.assertIsNone(ht.get("Dave"))



 
if __name__ == "__main__":
     unittest.main(verbosity=2)
