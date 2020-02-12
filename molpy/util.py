
def distance(point1, point2):
    """
        Calculate distance between two points.

        Parameters
        ----------
        point1 : array_like
            The first point.
        point2 : array_like
            The second point.

        Returns
        -------
        distance : float
            The distance between point1 and point2.
        """
    return sum([(x1 - x2) ** 2 for x1, x2 in zip(point1, point2)]) ** 0.5
