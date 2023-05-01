'''
Task:
Implement a decorator that logs the execution time of a function: Write a decorator that takes a function as an argument and logs the execution time of the function.
'''

import time
from datetime import datetime

def log(log_str: str) -> None:
    '''This function prints information to the console in addition with the associated datatime.
    
    > Example

    `LOG 2023-04-30 20:17:59.691428: Hello World`

    '''
    
    print(f'LOG {datetime.now()}: {log_str}')

# decorator for the timer
def my_decorator(func):

    # wrapper funciton
    def my_timer():

        start = datetime.now()                          # start the clock
        func()                                          # call the function
        end = datetime.now()                            # stop the clock 

        log(f'{func} execution time took a total of {end - start} seconds.')

    return my_timer

@my_decorator
def my_function() -> None:

    x = 0
    time.sleep(1) # simulate work performed
    x = 1

my_function()