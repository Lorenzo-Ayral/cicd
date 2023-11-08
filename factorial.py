"""
Module permettant de calculer la factorielle d'un nombre
"""

import time

final_list = []

def factorial(n):
    """
    Cette fonction permet de calculer la factorielle d'un nombre

    Args:
        n (int): nombre dont on veut calculer la factorielle

    Returns:
        int: factorielle du nombre n
    """
    time.sleep(.1)
    factorial = 1

    for i in range (1,n+1):
        factorial = factorial * i

    return factorial

def sum_factorial():
    """
    Cette fonction permet de calculer la factorielle de 50

    Returns:
        int: somme des factorielles de 0 à 50
    """
    for i in range(50):
        final_list.append(factorial(i))
    result=sum(final_list)
    print(f"Final SUM = {result}")

    return result

if __name__ == "__main__":
    sum_factorial()
