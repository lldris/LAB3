from typed_input import *

# 2 => 2.0
# float => integer

def main():
    """ Collect input data from the user and check datatype """
    first_term_a = input_type(float, "Enter first_term_a: ")
    common_difference = input_type(float, "Enter common_difference: ")
    n_terms = input_type(int, "Enter n_terms:")

    while n_terms <= 0:
        if n_terms == 0:
            n_terms = input_type(float, "n_terms cannot be 0. Enter n_terms: ")
        else:
            n_terms = input_type(float, "n_terms must be positive. Enter n_terms: ")

    arithmetic = artihmetic_sum(first_term_a, common_difference, n_terms)
    first_term_g = input_type(float, "Enter first_term_g: ")
    common_ratio = input_type(float, "Enter common_ratio: ")

    while common_ratio <= 1:
        if common_ratio == 1:
            common_ratio= input_type(float, "Common_ratio cannot be equal to 1. Enter common_ratio: ")
        elif common_ratio == 0:
            common_ratio= input_type(float, "Common_ratio cannot be equal to 0. Enter common_ratio: ")
        else:
            common_ratio = input_type(float, "Common_ratio cannot be negative. Enter common_ratio: ")

    geometric = geometric_sum(first_term_g, common_ratio, n_terms)

    """ Compare whether the arithmetic or geometric sum is larger """
    if artihmetic_sum(first_term_a, common_difference, n_terms) > geometric_sum(first_term_g, common_ratio, n_terms):
        print("The arithmetic sum is the biggest.")
    elif artihmetic_sum(first_term_a, common_difference, n_terms) < geometric_sum(first_term_g, common_ratio, n_terms):
        print("The geometric sum is the biggest.")
    else:
        print("The sums are equal")


if __name__ == "__main__":
    main()
