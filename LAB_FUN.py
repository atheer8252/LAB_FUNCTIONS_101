def print_pattern(n: int):
    """
    Function Name: print_pattern

    Description:
    This function takes one integer parameter (n) and prints
    a descending number pattern starting from n down to 1.
    Each row starts from the current number and decreases to 1.

    Parameter:
    n (int): A positive integer that represents the starting number of the pattern.

    Returns:
    None
    """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# Print the documentation of the function
print(print_pattern.__doc__)