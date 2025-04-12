def euclidean_algorithm_steps(a, b):
    print("How It Works (Step-by-Step):\n")
    print(f"Let's say we want to find gcd({a}, {b}):\n")
    
    step = 1
    while b != 0:
        quotient = a // b
        remainder = a % b
        print(f"{step}. Divide {a} by {b}:\n")
        print(f"   {a} ÷ {b} = {quotient} remainder {remainder} ⇒ gcd({a}, {b}) = gcd({b}, {remainder})\n")
        a, b = b, remainder
        step += 1

    print("Final Answer:\n")
    print(f"   gcd = {a}")

# Example usage
if __name__ == "__main__":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    euclidean_algorithm_steps(x, y)
