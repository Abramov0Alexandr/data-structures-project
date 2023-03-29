class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    test_list = []

    def __init__(self, head=None, end=None):

        self.head = head
        self.end = end

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        beginning_node = Node(data)

        if self.head is None:
            self.end = beginning_node

        else:
            beginning_node.next_node = self.head

        self.head = beginning_node

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        end_node = Node(data)
        if self.head is None:
            self.head = end_node

        else:
            self.end.next_node = end_node
        self.end = end_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        return ll_string.strip()
