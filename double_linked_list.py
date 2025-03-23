def get_double_linked_list(items):
    linked_list = DoubleLinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list


class DoubleLinkedListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        # Делаем новый узел головой
        new_node = DoubleLinkedListNode(value, self.head)

        # Если есть голова, добавляем ей в предшествующую ноду текущую
        if self.head:
            self.head.previous = new_node

        self.head = new_node
        # Если нет хвоста, этот узел будет и хвостом
        if self.tail is None:
            self.tail = new_node

        return self

    def append(self, value):
        new_node = DoubleLinkedListNode(value)

        # Если нет головы, этот узел будет головой
        if self.head is None:
            self.head = new_node
            self.tail = new_node

            return self

        # Присоеденяем новый узел к концу
        # Добавляем ссылку на предыдущий элемент в новую ноду
        # Делаем новую ноду хвостом

        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

        return self

    def delete(self, value):  # noqa: C901
        if self.head is None:
            return None

        deleted_node = None
        current_node = self.head

        while current_node:
            if current_node.value == value:
                deleted_node = current_node

                if deleted_node == self.head:
                    # Если голова должна быть удалена
                    # Устанавливаем голову на следующий узел
                    self.head = deleted_node.next

                    if self.head:
                        self.head.previous = None

                    if deleted_node == self.tail:
                        self.tail = None
                elif deleted_node == self.tail:
                    # Если хвост должен быть удален
                    # Устанавливаем хвост на предыдущий узел
                    self.tail = deleted_node.previous
                    self.tail.next = None
                else:
                    # Удаление центральных (не голова и не хвост) нод
                    previous_node = deleted_node.previous
                    next_node = deleted_node.next

                    previous_node.next = next_node
                    next_node.previous = previous_node

            current_node = current_node.next

        return deleted_node

    def find(self, value):
        if self.head is None:
            return None

        current_node = self.head

        while current_node:
            if value is not None and current_node.value == value:
                return current_node

            current_node = current_node.next

        return None

    def to_array(self):
        result = []
        if self.head is None:
            return result
        current_node = self.head
        while current_node:
            if current_node.value is not None:
                result.append(current_node.value)
            current_node = current_node.next
        return result


def solution(items):
    if not items:
        return []

    double_linked_list = get_double_linked_list(items)

    current_head = double_linked_list.head
    new_head = current_head.next

    new_head.previous = None

    current_head.previous = new_head
    current_head.next = new_head.next
    new_head.next = current_head

    double_linked_list.head = new_head

    return double_linked_list.to_array()


items = [[10, 20], 0, -1, ['hey']]

print(solution(items))  # [0, [10, 20], -1, ['hey']]
print(solution([]))  # []
