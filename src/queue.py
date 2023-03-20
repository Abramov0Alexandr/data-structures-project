class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""

        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        new_node = Node(data, None)

        if self.tail is not None:
            self.tail.next_node = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди и его возвращения

        :return: данные удаленного элемента
        """
        data = self.head.data
        self.head = self.head.next_node

        if self.head is None:
            self.tail = None
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        result = []
        node = self.head

        while node is not None:
            result.append(str(node.data))
            node = node.next_node

        return "\n".join(result)
