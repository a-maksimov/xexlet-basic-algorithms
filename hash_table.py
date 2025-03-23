class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

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


class Hash:
    def __init__(self):
        self.table = []
        self.count = 0

    def hash(self, s):
        k = 65537
        m = 2**20

        result = 0
        power = 0
        for i in range(len(s)):
            result = (result + power * ord(s[i])) % m
            power = (power * k) % m

        return result

    def calculate_index(self, table, key):
        try:
            return self.hash(str(key)) % len(table)
        except ZeroDivisionError:
            return self.hash(str(key))

    def rebuild_table_if_need(self):
        if len(self.table) == 0:
            self.table = [None for _ in range(128)]
        else:
            load_factor = self.count / len(self.table)

            if load_factor >= 0.8:
                new_table = [None for _ in range(len(self.table) * 2)]
                for list_ in self.table:
                    for pair in list_:
                        new_index = self.calculate_index(new_table, pair['key'])
                        if new_table[new_index] is None:
                            new_table[new_index] = LinkedList()

                        new_table[new_index].append(pair)

                self.table = new_table

    def set(self, key, value):
        self.rebuild_table_if_need()

        index = self.calculate_index(self.table, key)

        if self.table[index] is None:
            self.table[index] = LinkedList()

        self.table[index].append(
            {'key': key, 'value': value}
        )
        self.count += 1

    def get(self, key):
        index = self.calculate_index(self.table, key)
        if self.table[index] is None:
            return None

        for pair in self.table[index]:
            if pair['key'] == key:
                return pair['value']

        return None


def remove(hash, key):
    value = hash.get(key)
    if value is None:
        return None

    index = hash.calculate_index(hash.table, key)
    hash.table[index] = None

    return value


def solution(map, key):
    hash = Hash()

    for key_, value in map.items():
        hash.set(key_, value)

    return remove(hash, key)


table = Hash()
table.set("key", "value")
table.set("key1", "value1")

removed = solution(table, "key")
print(removed)  # => value

# В хеше ключа больше нет
table.get("key")  # None