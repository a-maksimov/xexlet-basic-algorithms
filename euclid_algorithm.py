def solution(a, b):
    if a == b:
        return a

    if b > a:
        a, b = b, a

    return solution(a - b, b)


print(solution(38, 28))  # => 2
print(solution(129, 90))  # => 3
