from decimal import Decimal
import math
 
def squared_power_list(value, *, start=0, end=5):
    """ Raises the value to the power of all items in a specified range of start and end (inclusive)  

    Parameters:
        value - value whose power is be calculated
        start - starting value of the list
        end - last value of the list

    Return:
        list of calculated powers

    """
    if not isinstance(value, int):
        raise ValueError(f"Power value not an instance of integer:'{value}")

    elif start >= end:
        raise ValueError("Start value is less than end value")

    elif start < 0 or end < 0:
        raise ValueError("Range values must not be negative")


    my_list = [item for item in range(start, end+1)] 
    power_list = [value**item for item in my_list]
    print(power_list)
    return power_list
    



def polygon_area(side_length, *, sides=3):
    """ Returns the area of a regular polygon

    Parameters:
        side_length: Length of side of regular polygon
        sides: number of sides

    """
    
    if not isinstance(side_length, (int, float)):
        raise ValueError(f"Length of side is not float or integer:'{side_length}")

    if not isinstance(sides, int):
        raise ValueError(f"Number of sides is not integer:'{sides}")

    if side_length < 0  or sides < 0:
        raise ValueError("Side length or number of sides must not be negative")

    if sides > 6:
        raise ValueError("Area is calculated for regular polygons of side length <=6") 

    area = (side_length**2 * sides)/(4 * math.tan(math.pi/sides))
    print(area)
 
    return round(area,5)

def temp_converter(base_temp, *, temp_given_in='f'):
    """ Converts base_temp to Fahrenheit if temp_given_in is Celsius and vice versa

    Parameters:
        base_temp Temperature to be converted
        temp_given_in Unit of base_temp

    """ 
    
    if not isinstance(base_temp, (int, float)):
        raise ValueError(f"Base temperature is not float or integer:'{base_temp}")

    if not isinstance(temp_given_in, str):
        raise ValueError(f"Unit of temperature is not string:'{temp_given_in}")

    if temp_given_in not in ['c', 'f']:
        raise ValueError("Unit of temperature must be c (Celsius) or f(Fahrenheit)")

    converted_temp = ((base_temp * 1.8) + 32) if temp_given_in == 'c' else (base_temp - 32) / 1.8
    print(converted_temp)

    return converted_temp
    

def speed_converter(speed, dist='km', time='min'):
    """Returns *speed* converted into specified *dist*/*time*

    Parameters:
        speed : value to be converted
        dist : unit of distance 
        time : unit of time

    """
    distance_conversion = {"km" : 1, 'm' : 1000, 'ft' : 3280.84, 'yrd' : 1093.61}
    time_conversion = {"ms" : 3.6e6, "s" : 3600, "min" : 60, "day" : 0.04166, "hr" : 1} 


    if not isinstance(speed, (int, float)):
        raise ValueError(f"Speed is not int/float:'{speed}")

    if speed < 0:
        raise ValueError("Speed cannt be negative")

    if dist not in distance_conversion:
        raise ValueError(f"Invalid unit of distance")

    if time not in time_conversion:
        raise ValueError(f"Invalid unit of time")

    converted_speed = speed * (distance_conversion[dist] / time_conversion[time])
    return round(converted_speed,3)
    
