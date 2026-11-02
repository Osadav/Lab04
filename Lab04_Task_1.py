# Print my header information
print("\n")
print("\"1 December 1918\" University of Alba Iulia")
print("Computer Science Department")
print("Course: Fundamental Algorithms")
print("Lab 4: Question 1 - Goldbach's Conjecture Decomposition for Even Numbers")
print("By: Osatohanmwen Davidson Ikponmwenosa")
print("\n")


# ---------------------------------------------------------
# 1. Develop a Python application that, for an even number entered by the user, finds the 
# decompositions described by Goldbach's conjecture: every even integer greater than 2 can be 
# expressed as the sum of two prime numbers.
# ---------------------------------------------------------

# Declare a variable to hold the user input
target = int(input("Enter an even number greater than 2: "))

# Define a function to check if a number is prime
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Define a function to find all pairs of prime numbers that sum to the given even number
def goldbach_pairs(even_number):
    """Finds all pairs of prime numbers that sum to the given even number."""
    if even_number <= 2 or even_number % 2 != 0:
        return "Please provide an even integer greater than 2."
    
    # Initialize a list to hold the pairs of prime numbers
    pairs = []

    # Loop through all numbers from 2 to even_number // 2 to find prime pairs
    for p1 in range(2, (even_number // 2) + 1):
        if is_prime(p1):
            p2 = even_number - p1
            if is_prime(p2):
                pairs.append((p1, p2))
                
    return pairs

# Call the function and print the result
print(f"Prime pairs for {target}: {goldbach_pairs(target)}")