class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    data_list: list = []

    def __init__(self, head=None, end=None):

        self.head = head
        self.end = end

    def insert_beginning(self, data: dict):
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.__verify_data(data):
            beginning_node = Node(data)

            if self.head is None:
                self.end = beginning_node

            else:
                beginning_node.next_node = self.head

            self.head = beginning_node

    def insert_at_end(self, data: dict):
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        if self.__verify_data(data):
            end_node = Node(data)
            if self.head is None:
                self.head = end_node

            else:
                self.end.next_node = end_node
            self.end = end_node

    def to_list(self):
        """Метод добавляет все значения узлов в список data_list"""
        node = self.head

        while node.next_node is not None:
            self.data_list.append(node.data)
            node = node.next_node

        self.data_list.append(node.data)
        return self.data_list

    def get_data_by_id(self, id_value) -> dict:
        """Метод позволяет получить элемент по его id из списка data_list"""
        for i in self.data_list:
            if i['id'] == id_value:
                return i

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

    @staticmethod
    def __verify_data(data):
        """Метод для проверки допустимости значений перед добавлением их в узел"""
        if isinstance(data, dict) and data.get('id') is not None:
            return True
        print('Данные не являются словарем или в словаре нет ключа "id"')
