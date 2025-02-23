def get_linked_list_from_array(items):
    linked_list = LinkedList()

    for value in items:
        linked_list.append(value)

    return linked_list


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        # Делаем новый узел головой
        new_node = LinkedListNode(value, self.head)
        self.head = new_node

        # Если нет хвоста, этот узел будет и хвостом
        if not self.tail:
            self.tail = new_node

        return self

    def append(self, value):
        new_node = LinkedListNode(value)

        # Если нет головы, этот узел будет головой
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return self

        # Присоеденяем новый узел к концу, делаем его хвостом
        self.tail.next = new_node
        self.tail = new_node
        return self

    def delete(self, value):  # noqa: C901
        if not self.head:
            return None

        deleted_node = None
        # Проверяем с головы какие ноды надо удалять
        while self.head and self.head.value == value:
            deleted_node = self.head
            self.head = self.head.next

        current_node = self.head

        # Если у головы не нашли, проверяем остальные значения в списке
        if current_node is not None:
            while current_node.next:
                if current_node.next.value == value:
                    deleted_node = current_node.next
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next

        # Проверяем хвост
        if self.tail.value == value:
            self.tail == current_node

        return deleted_node

    def find(self, value):
        if not self.head:
            return None

        current_node = self.head

        # Перебираем список с головы, первое найденное значение возвращаем
        while current_node:
            if current_node.value is not None and current_node.value == value:
                return current_node

            # Делаем текущей следующий элемент списка
            current_node = current_node.next

        return None

    def is_empty(self):
        return self.head is None and self.tail is None

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


def solution(items: list) -> list:
    if not items:
        return []

    def find_tail(node: LinkedListNode, reversed_head: LinkedListNode):
        if node.next is None:
            return reversed_head

        reversed_node = find_tail(node.next, reversed_head)
        reversed_node.next = LinkedListNode(node.value)

        return reversed_node.next

    linked_list = get_linked_list_from_array(items)

    head = linked_list.tail
    tail = find_tail(linked_list.head, head)

    reversed_linked_list = LinkedList()
    reversed_linked_list.head = head
    reversed_linked_list.tail = tail

    return reversed_linked_list.to_array()


items = [[10, 20], 0, -1, ['hey']]
print(solution(items))  # [['hey'], -1, 0, [10, 20]]

# def solution(items):
#     linked_list = get_linked_list_from_array(items)
#     reversed_list = LinkedList()
#
#     if not linked_list.head:
#         return reversed_list.to_array()
#
#     reversed_list.prepend(linked_list.head.value)
#     next_node = linked_list.head.next
#     while next_node:
#         reversed_list.prepend(next_node.value)
#         next_node = next_node.next
#     return reversed_list.to_array()
