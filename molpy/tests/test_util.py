import molpy
import pytest


@pytest.mark.parametrize("point1, point2, bench", [([0, 1], [0, 0], 1), ([0, 1, 2], [0, 1, -2], 4)])
def test_distance(point1, point2, bench):

    assert molpy.util.distance(point1, point2) == pytest.approx(bench, abs=1.e-6)
