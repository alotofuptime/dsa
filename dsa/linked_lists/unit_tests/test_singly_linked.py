import unittest
import pytest
from dsa.linked_lists.singly_linked import LinkedList, ListNode

class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.llist = LinkedList()

    def test_empty_list(self):
        self.assertIsInstance(self.llist, LinkedList)
        self.assertIsNone(self.llist.head)
        self.assertEqual(self.llist.size, 0)

    def test_empty_node(self):
        node = ListNode()
        self.assertIsNotNone(node.data)
        self.assertIsNone(node.next)

    def test_create_list_with_head_value(self):
        self.llist = LinkedList(9)
        self.assertIsInstance(self.llist.head, ListNode)
        self.assertIsNotNone(self.llist.head)
        self.assertIsNone(self.llist.head.next)
        self.assertEqual(self.llist.head.data, 9)
        self.assertEqual(self.llist.size, 1)

    def test_create_node_with_next_value(self):
        node = ListNode(9, 10)
        self.assertEqual(node.data, 9)
        self.assertEqual(node.next.data, 10)
        self.assertIsInstance(node.next, ListNode)

    def test_create_list_with_head_value_of_type_node(self):
        node = ListNode(9)
        self.llist.head = node
        self.assertEqual(str(self.llist.head), "Node(9)")
        self.assertIsInstance(self.llist.head.data, int)

    def test_set_head_with_empty_list(self):
        self.llist = LinkedList()
        self.llist.head = 8
        self.assertEqual(self.llist.head.data, 8)
        self.assertEqual(self.llist.size, 1)
        self.assertIsNone(self.llist.head.next)

    def test_set_head_to_node_obj_in_empty_list(self):
        node = ListNode(9)
        self.llist.head = node
        self.assertEqual(str(self.llist.head), "Node(9)")
        self.assertIsInstance(self.llist.head.data, int)

    def test_update_node_next_to_new_value(self):
        node = ListNode(9)
        self.llist.head = node
        node.next = 11
        self.assertEqual(self.llist.head.next.data, 11)
        self.assertIsInstance(self.llist.head.next, ListNode)

    def test_update_node_next_to_new_node(self):
        node = ListNode(9)
        node.next = ListNode(11)
        self.assertEqual(node.next.data, 11)

    def test_create_node_with_null_value(self):
        node = ListNode(None)
        self.assertEqual(node.data, 0)

    def test_create_node_with_node_obj_as_data(self):
        node = ListNode(ListNode(9))
        self.assertEqual(node.data, 9)

    def test_update_node_data_to_new_value(self):
        node = ListNode(9)
        node.data = 10
        self.assertEqual(node.data, 10)

    def test_update_node_data_to_null_value(self):
        node = ListNode(9)
        node.data = None
        self.assertEqual(node.data, 0)


  #  def test_set_head(self, data):
   #     self.llist.head = data
#        self.assertEqual(self.llist.head, data)




if __name__ == "__main__":
    unittest.main()
