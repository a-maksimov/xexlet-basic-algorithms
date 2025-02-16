def solution(number):
    if number == 1:
        return False
    for i in range(2, int(number ** 0.5)):
        if number % i == 0:
            return False
    return True


print(solution(1))
print(solution(2147483648))  # False
print(solution(87178291199))  # True
