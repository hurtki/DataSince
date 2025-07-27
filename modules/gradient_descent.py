import math
from typing import Callable


def gradient_decent(
    nigzeret: Callable[[float], float],
    start: float,
    alpha: float,
    iter: int,
    time_log: int
) -> float:
    """
    This function realizes a gradient decent algorithm 
    """
    # assighning unreal previous to not quit from the start
    previous = start + 999999
    # starting trying from start point
    x = start

    # entering cycle for iter
    for i in range(iter):
        # counting nigzerert volume from the given function
        value = nigzeret(x)

        # checking if we need to log somethink
        if i % (iter // time_log) == 0:
            print(f"value: {value}, x: {x}")

        # assighning new x value
        x -= alpha * value
        previous = value

    return x

