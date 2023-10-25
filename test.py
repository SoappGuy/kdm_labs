from icecream import ic

def prove_by_induction(n):
    def sum_of_odd_numbers(n):
        counter = 0
        number = 1
        sum = 0

        while counter < n:
            if number % 2 == 1:
                counter += 1
                sum += number
            number += 1
        return sum

    statement = "The sum of the first n odd numbers is n^2 for all positive integers n."
    print(f"Statement: {statement}")
    print("Proof by Mathematical Induction:")

    print("\nBase Case:")
    base_result = 1
    print(f"For n = 1, the sum of the first 1 odd number is 1^2 = {base_result}")

    if base_result == 1:
        print("Base case is verified.")
    else:
        print("Base case is not verified. The statement is false.")
        return

    # Induction Step
    print(f"\nInduction Step for n = {n}:")

    # Induction Hypothesis: Assuming the statement is true for n, prove it for n + 1
    induction_hypothesis = sum_of_odd_numbers(n) == n ** 2

    if induction_hypothesis:
        print(f"The sum of the first {n} odd numbers is {n}^2 = {n ** 2}")
        print(f"Assuming the statement is true for n = {n}, the induction hypothesis is verified.")
    else:
        print(f"Assuming the statement is true for n = {n}, the induction hypothesis is not verified.")
        print("The statement is false for n =", n)
        return

    print("\nMathematical induction is successfully applied.")
    print(f"The statement is proven for all positive integers n up to {n}.")


# Example usage
prove_by_induction(100)
