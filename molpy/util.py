
def distance(point1, point2):
    return sum([(x1 - x2) ** 2 for x1, x2 in zip(point1, point2)]) ** 0.5
