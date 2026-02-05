num = int(input('Enter a number'))

def prime_check(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

prime = prime_check(num)
print('{0} is a PRIME number', prime)