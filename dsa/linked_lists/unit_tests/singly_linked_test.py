import unittest
from dsa.linked_lists import singly_linked

class TestInsertionMethods(unittest.TestCase):
    def test_prepend_single_value(self):
        llist = singly_linked.LinkedList()
        llist.prepend(9)
        self.assertEqual(llist.size, 1)
        self.assertFalse(llist.is_empty())
        self.assertIs(llist.head, llist.tail)
        self.assertEqual(str(llist), str(9))

    def test_prepend_multi_values(self):
        llist = singly_linked.LinkedList()
        llist.prepend(10)
        llist.prepend(17)
        llist.prepend(15)
        llist.prepend(13)
        self.assertEqual(llist.size, 4)
        self.assertFalse(llist.is_empty())
        self.assertEqual(llist.head.val, 13)
        self.assertEqual(llist.tail.val, 10)

    def test_append_single_value(self):
        pass

    def test_append_multi_values(self):
        pass


class TestSearchMethods(unittest.TestCase):
    def test_search(self):
        llist = singly_linked.LinkedList()
        llist.prepend(9)
        llist.prepend(4)
        llist.prepend(8)
        llist.prepend(7)
        self.assertFalse(llist.search(10))
        self.assertTrue(llist.search(8))


if __name__  == "__main__":
    unittest.main()
