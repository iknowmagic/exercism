def square(number) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number-1)


def total():
    grains_total = 0
    for i in range(1, 65):
        grains_total += square(i)
    return grains_total
