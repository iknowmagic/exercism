def leap_year(year) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True

    return False
