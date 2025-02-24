def is_even(number):
    # U (Understand the problem): We need to check if a given number is even.
    # C (Create a plan): We will use the modulo operator (%) to determine if the remainder is zero.
    # A (Analyze the plan): If number % 2 == 0, then the number is even.
    # S (Solve the problem): Return the result of that check as True or False.
    # E (Evaluate the solution): We can test with various inputs to verify correctness.
    return number % 2 == 0
print(is_even(4))  # returns true
print(is_even(5))  # returns false

