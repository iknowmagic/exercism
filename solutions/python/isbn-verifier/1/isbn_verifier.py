def is_valid(isbn):
    numbers = [n for n in isbn if n not in ('-')]
    if len(numbers) != 10:
        return False
    for i,n in enumerate(numbers):
        if i != len(numbers) - 1 and not n.isdigit():
            return False
    if not (numbers[-1] == 'X' or numbers[-1].isdigit()):
        return False
    if numbers[-1] == 'X':
        numbers[-1] = 10
    numbers = [int(n) for n in numbers]
    total = sum(n * w for n, w in zip(numbers, range(10, 0, -1)))
    return total % 11 == 0
