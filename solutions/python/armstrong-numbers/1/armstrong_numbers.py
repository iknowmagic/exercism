def is_armstrong_number(number):
    number_parts = str(number)
    total = 0
    number_parts_length = len(number_parts)
    for num in number_parts:
        total += int(num)**number_parts_length

    return total == number
