import pytest
from task1.shape import Circle, Triangle, calculate_area

triangle_values = [(3, 4, 5, 6), (5, 6, 7, 15), (8, 17, 15, 60), (9, 12, 15, 54)]
circle_values = [(5, 79), (1, 3), (8, 201), (4.2, 55)]


@pytest.mark.parametrize('r, expected', circle_values)
def test_get_square_circle(r, expected):
    circle = Circle(r)
    assert calculate_area(circle) > 0
    assert round(calculate_area(circle)) == expected


@pytest.mark.parametrize('a, b, c, expected', triangle_values)
def test_get_square_triangle(a, b, c, expected):
    triangle = Triangle(a, b, c)
    assert calculate_area(triangle) > 0
    assert round(calculate_area(triangle)) == expected


def test_forbidden_values():
    with pytest.raises(ValueError):
        Circle(-3)
    with pytest.raises(TypeError):
        Circle('4')
    with pytest.raises(ValueError):
        Triangle(-2, 4, -1)
    with pytest.raises(ValueError):
        Triangle(4, 5, 100)
    with pytest.raises(TypeError):
        Triangle('2', 3, 4)


def test_is_rectangular():
    triangle = Triangle(17, 15, 8)
    assert triangle.is_rectangular() == True
