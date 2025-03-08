# Check if the input is even
def prove_even(n):
    print(f"Checking if {n} is even:")
    if n % 2 != 0:  # If n is odd, it should fail the even test
        print(f"1. {n} % 2 = {n % 2} (not 0) → {n} is odd, fails even test.")
        return False
    
    print(f"1. {n} % 2 = {n % 2} (0) → {n} is even.")
    squared = pow(n, 2)
    print(f"2. Square {n}: {n}^2 = {squared}")
    m = squared // 2  # Expressing squared as m
    print(f"3. Compute m: {squared} // 2 = {m}")
    
    result = squared == (2 * m)  # Ensures correct verification
    print(f"4. Verify: {squared} == 2 * {m} → {result}")
    return result

# Check if the input is odd
def prove_odd(n):
    print(f"Checking if {n} is odd:")
    if n % 2 == 0:  # If n is even, it should fail the odd test
        print(f"1. {n} % 2 = {n % 2} (0) → {n} is even, fails odd test.")
        return False
    
    print(f"1. {n} % 2 = {n % 2} (not 0) → {n} is odd.")
    squared = pow(n, 2)
    print(f"2. Square {n}: {n}^2 = {squared}")
    m = (squared - 1) // 2
    print(f"3. Compute m: ({squared} - 1) // 2 = {m}")
    
    result = squared == (2 * m + 1)  # Ensures proper odd number verification
    print(f"4. Verify: {squared} == 2 * {m} + 1 → {result}")
    return result

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

# Menu for user to choose proof type
while True:
    print("Choose the type of proof to perform:")
    print("1. Even/Odd Proof")
    print("2. Inequality Proof")
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        while True:
            user_input = input("Enter integers separated by spaces: ").strip()
            try:
                numbers = list(map(int, user_input.split()))
                break  # Valid input, exit loop
            except ValueError:
                print("Invalid input. Please enter valid integers.")
        
        for num in numbers:
            even_pass = prove_even(num)
            print(f"Result: {num} is even? {even_pass}\n")
            odd_pass = prove_odd(num)
            print(f"Result: {num} is odd? {odd_pass}\n")
        break
    
    elif choice == "2":
        while True:
            y_input = input("\nEnter two positive numbers separated by a space to test the inequality x/y + y/x ≥ 2: ").strip()
            try:
                x, y = map(float, y_input.split())
                if x > 0 and y > 0:
                    print("Proof result:", prove_inequality(x, y))
                    break  # Valid input, exit loop
                else:
                    print("Both numbers must be positive.")
            except ValueError:
                print("Invalid input. Please enter two positive numbers.")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")
