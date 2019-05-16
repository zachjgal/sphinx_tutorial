def fizzbuzz():
    """ u already know what this is

    Counts from 1-100, printing the number, followed by 'fizz' if the number is
    divisible by 3, 'buzz' if the number is divisible by 5, and 'fizzbuzz' if
    the number is divisible by both 3 and 5.

    See :py:func:`dict_map`
    
    Args:
        None
    
    Returns:
        None
    """
    for i in range(1, 101):
        print(str(i), end=': ')
        if i % 3 == 0:
            print('fizz', end='')
        if i % 5 == 0:
            print('buzz', end='')
        print()