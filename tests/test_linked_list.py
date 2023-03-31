"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList, Node


class TestNodeCls(unittest.TestCase):
    def test_init_node(self):
        test_node = Node()
        self.assertIsNone(test_node.data)
        self.assertIsNone(test_node.next_node)


class TestLinkedList(unittest.TestCase):

    def test_init_node(self):
        test_linked_list = LinkedList()
        self.assertIsNone(test_linked_list.head)
        self.assertIsNone(test_linked_list.end)

    def test_first_insert_to_begin_ll(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 1})
        self.assertEqual(test_linked_list.head.data, {'id': 1})
        self.assertEqual(test_linked_list.end.data, {'id': 1})

    def test_insert_to_begin_ll_twice(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 1})
        test_linked_list.insert_beginning({'id': 2})
        self.assertEqual(test_linked_list.head.data, {'id': 2})
        self.assertEqual(test_linked_list.end.data, {'id': 1})

    def test_insert_to_end_ll(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_at_end({'id': 2})
        self.assertEqual(test_linked_list.end.data, {'id': 2})

    def test_insert_to_end_ll_twice(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 1})
        test_linked_list.insert_at_end({'id': 2})
        self.assertEqual(test_linked_list.end.data, {'id': 2})
        self.assertEqual(test_linked_list.head.data, {'id': 1})

    def test_empty_str(self):
        test_linked_list = LinkedList()
        self.assertIsNone(print(test_linked_list))

    def test_filled_ll_str(self):
        test_linked_list = LinkedList()
        test_linked_list.insert_beginning({'id': 1})
        test_linked_list.insert_at_end({'id': 2})
        self.assertEqual(str(test_linked_list), "{'id': 1} -> {'id': 2} -> None")

    def test_checking_data(self):
        test_ll = LinkedList()
        self.assertIsNone(test_ll.insert_beginning('test'))

    def test_to_list_method(self):
        test_ll = LinkedList()
        test_ll.insert_beginning({'id': 'test1'})
        test_ll.insert_at_end({'id': 'test2'})
        data_in_list = test_ll.to_list()
        self.assertEqual(data_in_list, [{'id': 'test1'}, {'id': 'test2'}])

    def test_get_data_by_id(self):
        new_test_ll = LinkedList()
        new_test_ll.insert_beginning({'id': 'WTF'})
        new_test_ll.to_list()
        user_data = new_test_ll.get_data_by_id('WTF')
        self.assertEqual(user_data, {'id': 'WTF'})



