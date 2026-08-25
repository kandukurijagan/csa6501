def factorial(n):
    if n < 0:
        return None

    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter Number: "))

result = factorial(num)

if result is None:
    print("Invalid Input")
else:
    print("Factorial =", result)
