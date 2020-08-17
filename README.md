# session5-timeit

Welcome to EPAi Session 5 assignment! 

This repo contains the following:
* time_it.py - Python file that contains the method to calculate average time of execution of functions over multiple runs
* functions.py - Python file that contains functions: squared_power_list, polygon_area, temp_converter, speed_converter

## Description

### time_it(fn,\*args, repetitions= 1, \*\*kwargs)
Returns the average run time per call. *repetitions*, if present must be a keyword argument. The default value of *repetitions* is 1. 
If *repetitions* are given as 0, then ValueError is thrown. 

All args and kwargs are passed to the function *fn* as arguments. 

### squared_power_list(value, \*, start=0, end=5)
Raises the value to the power of all items in a specified range of start and end (inclusive). Named arguments are *start* and *end*; positional is *value*
Raises ValueError for the following:
* *value* is not an integer
* *start* is greater than *end*
* *start* or *end* are negative

### polygon_area(side_length, \*, sides=3)
Returns the area of a regular polygon of length of side *side_length*(named) and number of sides *sides*(positional)
Raises ValueError for the following:
* *side_length* is not an integer or float
* *sides* is not an int or greater than 6
* *side_length* or *sides* are negative

### temp_converter(base_temp, \*, temp_given_in='f')
Returns base_temp(named) to Fahrenheit if temp_given_in(positional) is Celsius and vice versa
Raises ValueError for the following:
* *base_temp* is not an integer or float
* *temp_given_in* is not 'f'(Fahrenheit) or 'c' (Celsius)

### speed_converter(speed, dist='km', time='min')
Returns *speed* converted into specified *dist*/*time*. Named arguments are *dist* and *time*; postitional argument is *speed*.
Raises ValueError for the following:
* *speed* not integer or float
* *dist* not specified as 'km', 'm', 'yrd', 'ft' 
* *time* not specified as 'ms', 's', 'min', 'hr', 'day'


## Tests
Unit tests are written in pytest framework

### test_readme_exists
Checks if the ReadMe exists

### test_readme_contents
Ensures that the ReadMe contains atleast 500 words 

### test_readme_proper_description
Tests if all methods are described 

### test_readme_file_for_formatting
Checks if the file has headings and is formatted

### test_timeit_zerorep
Checks if ValueError is thrown for zero or negative repetitions

### test_timeit_print
Checks if the timeit method works correctly for print with sep='-', end= ' ***\n'

### test_squared_power_list_invalid_vals
Checks if ValueError is thrown for various invalid values

### test_squared_power_list_valid
Checks if squared_power_list returns the correct values 

###  test_timeit_squared_power
Checks if timeit returns a value greater than 0.1 for time_it(squared_power_list, 2, start=0, end=5, repetitions=5)

### test_polygon_area_invalid_vals
Checks if polygon_area throws a ValueError for invalid arguments

### test_polygon_area_valid
Checks if polygon_area returns the correct value for valid arguments

### test_timeit_polygon_area
Checks if the time is > 0.1 for time_it(polygon_area, 15, sides = 3, repetitions=10)

### test_speed_converter_invalid_values
Checks if ValueError is thrown for invalid values

### test_speed_converter_valid
Checks if correct value is returned for valid arguments

### test_timeit_speed_converter
Checks if time returned is > 0.1 for time_it(speed_converter, 100, dist='km', time='min', repetitions=200)

### test_timeit_withoutrepetitions
Checks if default value of repetitions works 
### test_temp_converter_invalid_values
Checks if ValueError is thrown for invalid values

### test_temp_converter_valid
Checks if correct value is returned for valid arguments

### test_timeit_temp_converter
Checks if time returned is > 0.1 for time_it(temp_converter, 100, temp_given_in = 'f', repetitions=100)

### test_timeit_withoutrepetitions
Checks if timeit works without repetitions





 

