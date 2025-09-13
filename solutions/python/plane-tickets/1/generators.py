"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    letters = ['A', 'B', 'C', 'D']
    for n in range(number):
        yield chr(65 + n % 4)

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    row = 1
    seat_count = 0
    for letter in generate_seat_letters(number):
        if seat_count == 4:
            seat_count = 0
            row += 1
            if row == 13:
                row = 14

        seat_count += 1
        yield f'{row}{letter}'

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    result = {}
    for i, seat_letter in enumerate(generate_seats(len(passengers))):
        result[passengers[i]] = seat_letter
    return result

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat_number in seat_numbers:
        code = f'{seat_number}{flight_id}'
        yield code.ljust(12, '0')