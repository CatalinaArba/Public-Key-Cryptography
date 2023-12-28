import math
import time

# Calculate the greatest common divisor using the Euclidean algorithm
def euclidean_gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) using the Euclidean algorithm.
    This algorithm repeatedly applies the modulo operation until the GCD is found.

    :param a: First number
    :param b: Second number
    :return: The GCD of the input numbers
    """
    while b:
        a, b = b, a % b
    return a

# Calculate the greatest common divisor using subtraction-based method
def substraction_gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) using a subtraction-based method.
    This method repeatedly subtracts the smaller number from the larger number until the GCD is found.

    :param a: First number
    :param b: Second number
    :return: The GCD of the input numbers
    """
    if b == 0 or a == 0:
        return max(a, b)
    if a == b:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# Calculate the greatest common divisor and Bézout coefficients using the extended Euclidean algorithm
def extended_gcd(a, b):
    """
    Calculates the greatest common divisor (GCD) and Bézout coefficients using the extended Euclidean algorithm.
    This algorithm finds the GCD and the values of x and y that satisfy the equation ax + by = GCD(a, b).

    :param a: First number
    :param b: Second number
    :return: A tuple containing the GCD and the Bézout coefficients (GCD, x, y)
    """
    x1, x2, y1, y2 = 1, 0, 0, 1

    while b:
        q, a, b = a // b, b, a % b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2

    return (a, x1, y1)

# Measure the execution time of each algorithm for various inputs
inputs = [(9, 6), (0, 5), (48, 18), (56, 48), (105, 30), (350, 700), (123456, 789), (1, 1), (12345, 54321), (987654321987654321, 123456789)]

for a, b in inputs:
    print(f"Input: ({a}, {b})")

    start_time = time.perf_counter_ns()
    result = euclidean_gcd(a, b)
    end_time = time.perf_counter_ns()
    print(f"Euclidean GCD: {result}, Execution Time: {end_time - start_time:} nanoseconds")

    start_time = time.perf_counter_ns()
    result = substraction_gcd(a, b)
    end_time = time.perf_counter_ns()
    print(f"Subtraction GCD: {result}, Execution Time: {end_time - start_time:} nanoseconds")

    start_time = time.perf_counter_ns()
    result = extended_gcd(a, b)[0]
    end_time = time.perf_counter_ns()
    print(f"Extended Euclidean GCD: {result}, Execution Time: {end_time - start_time:} nanoseconds")

    print("=" * 40)
