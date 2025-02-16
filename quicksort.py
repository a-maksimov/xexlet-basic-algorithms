def solution(items, order="asc"):
    if not items:
        return items

    middle = len(items) // 2
    pivot = items[middle]

    smaller = []
    larger = []

    for i, item in enumerate(items):
        if i == middle:
            continue
        elif item < pivot:
            smaller.append(item)
        else:
            larger.append(item)

    result_smaller = solution(smaller)
    result_larger = solution(larger)

    if order == "desc":
        result_smaller.reverse()
        result_larger.reverse()
        result_smaller, result_larger = result_larger, result_smaller

    return result_smaller + [pivot] + result_larger


items = [10, 20, 0, -1]

print(solution(items))  # [-1, 0, 10, 20]
print(solution([]))  # []
print(solution(items, 'desc'))  # [20, 10, 0, -1]
