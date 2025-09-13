def is_abundant(number):
    pass

def is_deficient(number):
    pass
def get_divisors(number):
    list = []
    d = number - 1
    while d > 0:
        if number % d == 0:
            list.append(d)
        d -= 1
    return list

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    divisors = get_divisors(number)
    aliquot_sum = sum(divisors)
    if aliquot_sum == number:
        return "perfect"    
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"