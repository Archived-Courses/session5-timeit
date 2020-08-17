import os
import math
import pytest
from timeit import *
from functions import *

README_CONTENT_CHECK_FOR = [
        "time_it",
        "positional",
        "named",
        "squared_power_list",
        "polygon_area",
        "temp_converter",
        "speed_converter",
        "ValueError",
        "test_readme_exists",
        "test_readme_contents",
        "test_readme_proper_description",
        "test_timeit_zerorep",
        "test_timeit_print",
        "test_squared_power_list_invalid_vals",
        "test_squared_power_list_valid",
        "test_timeit_squared_power",
        "test_polygon_area_invalid_vals",
        "test_polygon_area_valid",
        "test_timeit_polygon_area",
        "test_temp_converter_invalid_values",
        "test_temp_converter_valid",
        "test_timeit_temp_converter",
        "test_speed_converter_invalid_values",
        "test_speed_converter_valid",
        "test_timeit_speed_converter",
        "test_timeit_withoutrepetitions"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_timeit_zerorep():
    with pytest.raises(ValueError):
        time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=0)
        time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=-1)


def test_timeit_print():
    average_time = time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitions=10)
    assert(average_time > 0)

def test_timeit_withoutrepetitions():
    average_time = time_it(print, 1, 2, 3, sep='-', end= ' ***\n')
    assert(average_time > 0)

def test_squared_power_list_invalid_vals():
    with pytest.raises(ValueError):
        time_it(squared_power_list,'a', start=0, end=5, repetitions=5)
        time_it(squared_power_list,-3, start=0, end=5, repetitions=5)
        time_it(squared_power_list,2, start=10, end=5, repetitions=5)


def test_squared_power_list_valid():
    assert([1,2,4,8,16,32] == squared_power_list(2, start=0, end=5))


def test_timeit_squared_power():
    assert(0.0 < time_it(squared_power_list, 2, start=0, end=5, repetitions=5))

def test_polygon_area_invalid_vals():
    with pytest.raises(ValueError):
        polygon_area('a', sides = 3)
        polygon_area(15, sides = 'a')
        polygon_area(-2.5, sides = 3)
        polygon_area(15, sides = -3)
        polygon_area(15, sides = 7)


def test_polygon_area_valid():
    assert math.isclose(polygon_area(15, sides=3), 97.4279, rel_tol=1e-5)

def test_timeit_polygon_area():
    assert(0.0 < time_it(polygon_area, 15, sides = 3, repetitions=10) )


def test_temp_converter_invalid_values():
    with pytest.raises(ValueError):
        temp_converter('a', temp_given_in = 'f')
        temp_converter(15, temp_given_in = 'a')
        temp_converter(15, temp_given_in = 30)


def test_temp_converter_valid():
    assert(-20 == temp_converter(-4, temp_given_in = 'f'))
    assert(193.1 == temp_converter(89.5, temp_given_in = 'c'))

def test_timeit_temp_converter():
    assert(0.0 < time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100) )

def test_speed_converter_invalid_values():
    with pytest.raises(ValueError):
        speed_converter('a', dist = 'km', time = 'min')
        speed_converter(15, dist = 'a', time = 'min')
        speed_converter(15, dist = 'km', time = 'a')
        speed_converter(0, dist = 'km', time = 'min')


def test_speed_converter_valid():
    assert(2.778 == speed_converter(10, dist = 'm', time = 's'))
    assert(9.113 == speed_converter(10, dist = 'ft', time = 's'))
    assert(182.268 == speed_converter(10, dist = 'yrd', time = 'min'))
    assert(32808.4 == speed_converter(10, dist = 'ft', time = 'hr'))

def test_timeit_speed_converter():
    assert(0.0 < time_it(speed_converter, 100, dist='km', time='min', repetitions=200) )
    
def test_timeit_assertion_speed():
    with pytest.raises(TypeError):
        time_it(speed_converter, 100, dist='km', t='min', repetitions=200) 

def test_timeit_assertion_temp():
    with pytest.raises(TypeError):
        time_it(temp_converter, 100, temp_given = 'f', repetitions=100) 

def test_timeit_assertion_square():
    with pytest.raises(TypeError):
        time_it(squared_power_list, 2, start=0, e=5, repetitions=5)

def test_timeit_assertion_polygon():
    with pytest.raises(TypeError):
        time_it(polygon_area, 15, sid = 3, repetitions=10)

def test_timeit_noassertion_polygon_nonamed():
    time_it(polygon_area, 15, repetitions=10)

def test_timeit_assertion_polygon_nopositional():
    with pytest.raises(TypeError):
        time_it(polygon_area, sides = 3, repetitions=10)
