num = int(input('Enter the number you want to calculate factorial for'))

def factorial(n):
    if n == 1:
        return n
    return n * factorial(n-1)

fact_calc = factorial(num)
print("The factorial is: ", fact_calc)

