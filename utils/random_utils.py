# Standard Libraries
import random


def generate_random_number(length: int) -> int:
    if length < 1:
        raise ValueError("Length must be a positive integer")

    # Step #1: Ensure the first digit is non-zero to meet the length requirement
    first_digit = random.randint(1, 9)

    # Step #2: Generate the remaining digits
    generated_digits = []
    for _ in range(length - 1):
        generated_integer = random.randint(0, 9)
        generated_digits.append(generated_integer)

    # Step #3: Combine the digits into a single integer
    random_integer = int(str(first_digit) + ''.join(map(str, generated_digits)))
    return random_integer
