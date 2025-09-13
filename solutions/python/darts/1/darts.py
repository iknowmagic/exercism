import math


def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    points = 0
    if 5 < distance <= 10:
        points = 1
    elif 1 < distance <= 5:
        points = 5
    elif distance <= 1:
        points = 10
    return points
