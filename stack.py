class Stack:
    def __init__(self, items):
        self.items = list(items)

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return not self.items


def process_stack(stack):
    items = []
    while not stack.is_empty():
        item = stack.pop()
        if item == '#':
            process_stack(stack)
            if not stack.is_empty():
                stack.pop()
        else:
            items.append(item)

    return items


def solution(string1, string2):
    items1 = process_stack(Stack(string1))
    items2 = process_stack(Stack(string2))
    return items1 == items2


print(solution('ab#c', 'ab#c'))  # True
print(solution('ab##', 'c#d#'))  # True
print(solution('a#c', 'b'))  # False
print(solution('y#fo##f', 'y#f#o##f'))
