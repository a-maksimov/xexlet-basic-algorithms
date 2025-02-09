def solution(phonebook, name):
    if not phonebook:
        return 'Phonebook is empty!'

    left_index = 0
    right_index = len(phonebook) - 1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if phonebook[middle_index]["name"] == name:
            return phonebook[middle_index]["number"]

        if name < phonebook[middle_index]["name"]:
            right_index = middle_index - 1
        else:
            left_index = middle_index + 1

    return 'Name not found!'


phonebook = [
    {'name': 'Alex Bowman', 'number': '48-2002'},
    {'name': 'Aric Almirola', 'number': '10-1001'},
    {'name': 'Bubba Wallace', 'number': '23-1111'},
]

print(solution(phonebook, 'Alex Bowman'))  # '48-2002'
print(solution(phonebook, 'None'))  # 'Name not found!'
print(solution([], 'Alex Bowman'))  # 'Phonebook is empty!'
