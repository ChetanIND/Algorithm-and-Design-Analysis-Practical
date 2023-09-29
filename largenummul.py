# Write a python program to perform the large multiplication number.
def LargeMultiplication(x, y):
    # Define the base for the multiplication (base 10 for decimal numbers).
    base = 10

    # If one of the numbers is less than 10, perform simple multiplication.
    if x < 10 or y < 10:
        return x * y

    # Find the number of digits in the larger of the two numbers.
    num = max(len(str(x)), len(str(y)))

    # Calculate the number of digits in each half.
    half = num // 2

    # Split the numbers into their high and low parts.
    a = x // (base**half)  # High part of x.
    b = x % (base**half)  # Low part of x.
    c = y // (base**half)  # High part of y.
    d = y % (base**half)  # Low part of y.

    # Recursively compute the products of the high and low parts.
    ac = LargeMultiplication(a, c)
    bd = LargeMultiplication(b, d)

    # Calculate the cross product of the high and low parts.
    abcd = LargeMultiplication(a + b, c + d) - ac - bd

    # Calculate the final result using Karatsuba's formula.
    ans = (ac * (base ** (2 * half))) + (abcd * (base**half)) + (bd)

    return ans


if __name__ == "__main__":
    # Input two large numbers from the user.
    x = int(input("Enter Number1: "))
    y = int(input("Enter Number2: "))

    # Call the LargeMultiplication function to compute the result.
    ans = LargeMultiplication(x, y)

    # Print the result of the multiplication.
    print("Multiplication of numbers are: ", ans)
