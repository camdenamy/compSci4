def is_even(n):
    return n % 2 == 0


def prove_even(n):
    a = n // 2  # Expressing n as 2a
    squared = pow(n, 2)
    m = pow(a, 2)  # Expressing squared as 4m
    return squared == (4 * m)


def prove_odd(n):
    k = (n - 1) // 2  # Expressing n as 2k + 1
    squared = pow(n, 2)
    m = squared // 2  # Expressing squared as 2m + 1
    return squared == (2 * m + 1)


def prove_inequality(x, y):
    if x <= 0 or y <= 0:
        return "x and y must be positive real numbers."

    lhs = (x / y) + (y / x)
    rhs = 2
    proof_holds = lhs >= rhs

    print(f"For x = {x}, y = {y}:")
    print(f"  x/y + y/x = {lhs} ≥ {rhs} -> {proof_holds}")
    
    return proof_holds


# Menu for user to choose proof type
print("Choose the type of proof to perform:")
print("1. Even/Odd Proof")
print("2. Inequality Proof")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    # Lists to store numbers
    numbers = []
    even_numbers = []
    odd_numbers = []

    # Take all user inputs on one line
    user_input = input("Enter integers separated by spaces: ").strip()

    try:
        numbers = list(map(int, user_input.split()))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        exit()

    # Check and print proof results for all numbers
    for num in numbers:
        even_proof = prove_even(num)
        odd_proof = prove_odd(num)
        print("--------------------------------------------------\n")
        print(f"Number: {num}\n")
        
        # Even proof
        a = num // 2
        squared = pow(num, 2)
        m = pow(a, 2)
        print(f"       Proof for Even: {num} = 2a, a={a}")
        print(f"       {num}^2 = (2a)^2 = 4({m}) = {squared} -> {even_proof}\n")
        
        # Odd proof
        k = (num - 1) // 2
        squared = pow(num, 2)
        m = squared // 2
        print(f"       Proof for Odd: {num}^2 = (2k + 1)^2, k={k}")
        print(f"       = ((2({k})+1)^2 = {squared}")
        print(f"       = 2({m})+1 -> {odd_proof}\n")
        
        # Categorize number
        if even_proof:
            even_numbers.append(num)
            print(f"       \033[1mConclusion: {num} is even.\033[0m\n")
        if odd_proof:
            odd_numbers.append(num)
            print(f"       \033[1mConclusion: {num} is odd.\033[0m\n")
        print("--------------------------------------------------")

    # Print results
    print("\nProcessed numbers:", numbers)
    print("Even numbers:", even_numbers)
    print("Odd numbers:", odd_numbers)

elif choice == "2":
    # Take user input for inequality proof
    y_input = input("\nEnter two positive numbers separated by a space to test the inequality x/y + y/x ≥ 2: ").strip()
    try:
        x, y = map(float, y_input.split())
        prove_inequality(x, y)
    except ValueError:
        print("Invalid input. Please enter two positive numbers.")
else:
    print("Invalid choice. Please enter 1 or 2.")
