# This is an example file to practice my Git skills

def print_twice(text):
    """This is a simple function to print the given text twice.

    Args:
        text (str): param to be returned from func multiplied by 2
    """

    return ((text + " ") * 2).rstrip()


def multiply_n_numbers(list):
    """
    multiply_n_numbers _summary_

    _extended_summary_

    Args:
        list (list): list with numbers to be mutliplied

    Returns:
        int : the product of all numbers
    """

    current_num = 1
    for i in list:
        try:
            current_num *= i
        except ValueError:
            return "Not a number!"
    return current_num

print(multiply_n_numbers([1, 2, 3]))