def input_type(datatype, prompt):
    while True:
        if datatype == float:
            try:
                user_input = float(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a float.")
        
        elif datatype == int:
            try:
                user_input = int(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter an integer.")
        else:
            print("Invalid datatype")



def artihmetic_sum(first_term_a, common_difference, n_terms):
    """
    Calculates the arithmetic sum of a series.
    Parameters:
    first_term_a (int): The first term of the series.
    d (int): The difference between consecutive terms.
    n (int): The number of terms in the series.
    Returns:
    int: The sum of the arithmetic series.
    """
    sum = int(n_terms / 2 * (2 * first_term_a + common_difference * (n_terms - 1)))
    return sum


def geometric_sum(first_term_g, common_ratio, n_terms):
    """
    Calculates the geometric sum of a series.
    Parameters:
    first_term (int): The first term of the series.
    common_ratio (int): The common ratio between consecutive terms.
    n_terms (int): The number of terms in the series.
    Returns:
    int: The sum of the geometric series.
    """
    if common_ratio == 1:
        """Raise an expected exception. From: https://docs.python.org/3/tutorial/errors.html"""
        raise ValueError("common_ratio can't be equal to one")

    else:
        sum = int(first_term_g * (common_ratio**n_terms - 1) / (common_ratio - 1))
        return sum
