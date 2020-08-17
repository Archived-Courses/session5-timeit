import time

""" Python file that contains time_it method to calculate the time taken to execute a method"""


def time_it(fn, *args, repetitions= 1, **kwargs):
    """
    Function that gives out average run time per call

    Parameters:
        fn function to be called
        args positional arguments 
        kwargs named arguments
        repetitions number of times to run the method
    """
    total_time = 0

    if repetitions == 0:
        raise ValueError("Repetitions cannot be zero")
    for rep in range(repetitions):

        start_time = time.time()

        fn(*args, **kwargs)

        end_time = time.time()

        total_time = total_time + (end_time - start_time)

    return total_time/repetitions
