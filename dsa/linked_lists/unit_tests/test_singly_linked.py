import unittest
import pytest
from dsa.linked_lists.singly_linked import LinkedList, ListNode

class TestSinglyLinkedList(unittest.TestCase):

    llist = None

    def setUp(self):
        self.llist = LinkedList()

    def test_empty_list(self):
        self.assertIsInstance(self.llist, LinkedList)
        self.assertIsNone(self.llist.head)
        self.assertEqual(self.llist.size, 0)

    def test_create_list_with_head_value(self):
        self.llist = LinkedList(9)
        self.assertIsInstance(self.llist.head, ListNode)
        self.assertIsNotNone(self.llist.head)
        self.assertIsNone(self.llist.head.next)
        self.assertEqual(self.llist.head.data, 9)
        self.assertEqual(self.llist.size, 1)

    def test_set_head_with_empty_list(self):
        self.llist = LinkedList()
        self.llist.head = 8
        self.assertEqual(self.llist.head, 8)
        self.assertIsInstance(self.llist.head, ListNode)
        self.assertEqual(self.llist.size, 1)
        self.assertIsNone(self.llist.head.next)

  #  def test_set_head(self, data):
   #     self.llist.head = data
#        self.assertEqual(self.llist.head, data)




if __name__ == "__main__":
    unittest.main()
