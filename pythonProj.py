# Define the truth table function
def truthTable(expression):
    """
    Generates a truth table for the given boolean expression.
    Dynamically prompts the user for the number of inputs (2, 3, or 4).
    """
    inputs = int(input("Enter the number of inputs (2, 3, or 4): "))
    if inputs not in [2, 3, 4]:
        raise ValueError("Number of inputs must be 2, 3, or 4.")

    print("\nBoolean Expression:")
    print("  X = " + expression.upper())
    expression = expression.lower()

    # Replace strings with bitwise operators
    expression = expression.replace("and", "&")
    expression = expression.replace("xor", "^")
    expression = expression.replace("or", "|")
    expression = expression.replace("not", "~")

    # Print the Truth Table based on user input
    print("\nTruth Table:")
    if inputs == 2:
        print("  \033[1m-------------\033[0m")
        print("  \033[1m| A | B | X |\033[0m")
        print("  \033[1m-------------\033[0m")
        
        for a in range(0, 2):
            for b in range(0, 2):
                x = eval(expression)
                print(f"  | {chr(84 if a else 70)} | {chr(84 if b else 70)} | {chr(84 if x else 70)} |")
                print("  \033[1m-------------\033[0m")
    
    elif inputs == 3:
        print("  \033[1m-----------------\033[0m")
        print("  \033[1m| A | B | C | X |\033[0m")
        print("  \033[1m-----------------\033[0m")
        
        for a in range(0, 2):
            for b in range(0, 2):
                for c in range(0, 2):
                    x = eval(expression)
                    print(f"  | {chr(84 if a else 70)} | {chr(84 if b else 70)} | {chr(84 if c else 70)} | {chr(84 if x else 70)} |")
                    print("  \033[1m-----------------\033[0m")
    
    elif inputs == 4:
        print("  \033[1m---------------------\033[0m")
        print("  \033[1m| A | B | C | D | X |\033[0m")
        print("  \033[1m---------------------\033[0m")
        
        for a in range(0, 2):
            for b in range(0, 2):
                for c in range(0, 2):
                    for d in range(0, 2):
                        x = eval(expression)
                        print(f"  | {chr(84 if a else 70)} | {chr(84 if b else 70)} | {chr(84 if c else 70)} | {chr(84 if d else 70)} | {chr(84 if x else 70)} |")
                        print("  \033[1m---------------------\033[0m")

# Define the bitwise function
def bitwise_shift(value, shift_by, direction):
    """
    Perform a bitwise left or right shift on a given value.

    Args:
        value (int): The number to shift.
        shift_by (int): Number of places to shift.
        direction (str): 'left' for left shift or 'right' for right shift.

    Returns:
        result (int): The result of the bitwise shift.
    """
    if direction == 'left':
        shifted = value << shift_by
        calculated = value * (2 ** shift_by)
        print(f"{value} << {shift_by} = {shifted} (Expected: {calculated})")
        assert shifted == calculated, "Left shift does not match multiplication by 2^n"
        return shifted
    elif direction == 'right':
        shifted = value >> shift_by
        calculated = value // (2 ** shift_by)
        print(f"{value} >> {shift_by} = {shifted} (Expected: {calculated})")
        assert shifted == calculated, "Right shift does not match division by 2^n"
        return shifted
    else:
        raise ValueError("Direction must be 'left' or 'right'.")

 
# Call functions
expression = input("Enter a boolean expression (A OR (B AND C)): ")
truthTable(expression)

print("\nPerforming bitwise left shift:")
bitwise_shift(5, 3, 'left')

print("\nPerforming bitwise right shift:")
bitwise_shift(40, 3, 'right')
