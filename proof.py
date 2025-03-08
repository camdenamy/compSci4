def prove_even(n):
    """Checks if a number is even using mathematical proof."""
    if n % 2 != 0:  # If n is odd, it should fail the even test
        return False

    a = n // 2  # Expressing n as 2a
    squared = pow(n, 2)
    m = squared // 4  # Expressing squared as 4m

    return squared == (4 * m)  # Ensures correct verification


def prove_odd(n):
    """Checks if a number is odd using mathematical proof."""
    if n % 2 == 0:  # If n is even, it should fail the odd test
        return False

    k = (n - 1) // 2  # Expressing n as 2k + 1
    squared = pow(n, 2)
    m = (squared - 1) // 2  # Expressing squared as 2m + 1

    return squared == (2 * m + 1)  # Ensures proper odd number verification

def prove_inequality(x, y):
    if x <= 0 or y <= 0:
        return "x and y must be positive real numbers."

    lhs = round((x / y) + (y / x), 2)
    rhs = 2
    proof_holds = lhs >= rhs

    print(f"Step-by-step proof for inequality x/y + y/x ≥ 2:")
    print(f"1. Compute x/y: {x} / {y} = {round(x/y, 2)}")
    print(f"2. Compute y/x: {y} / {x} = {round(y/x, 2)}")
    print(f"3. Add both terms: {round(x/y, 2)} + {round(y/x, 2)} = {lhs}")
    print(f"4. Compare with 2: {lhs} ≥ {rhs} -> {proof_holds}")
    return proof_holds


def print_table(results):
    """Prints results in a tabular format."""
    print("\nResults:")
    print("---------------------------------------")
    print(f"{'Number':<8} {'Pass Even Test':<15} {'Pass Odd Test':<15}")
    print("---------------------------------------")

    for result in results:
        num, even_pass, odd_pass = result
        print(f"{num:<8} {str(even_pass):<15} {str(odd_pass):<15}")

    print("---------------------------------------")


# Menu for user to choose proof type
print("Choose the type of proof to perform:")
print("1. Even/Odd Proof")
print("2. Inequality Proof")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    # Take all user inputs on one line
    user_input = input("Enter integers separated by spaces: ").strip()

    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit()

    # Check and print proof results for all numbers
    results = []
    for num in numbers:
        even_pass = prove_even(num)
        odd_pass = prove_odd(num)

        # Store results
        results.append((num, even_pass, odd_pass))

    # Print the table of results
    print_table(results)

elif choice == "2":
    # Take user input for inequality proof
    y_input = input("\nEnter two positive numbers separated by a space to test the inequality x/y + y/x ≥ 2: ").strip()
    try:
        x, y = map(float, y_input.split())
        print("Proof result:", prove_inequality(x, y))
    except ValueError:
        print("Invalid input. Please enter two positive numbers.")
else:
    print("Invalid choice. Please enter 1 or 2.")
