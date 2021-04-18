"""Fact Logic   n * (n-1)"""
def factorial_iterative(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3..........1
    """
    fact = 1
    for i in range(n):
        fact = fact * (i+1)
    return fact


number = int(input("Enter the number : "))
print("factorial using Iterative: ", factorial_iterative(number))
