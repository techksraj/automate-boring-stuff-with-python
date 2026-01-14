def div42by(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print('Error: You tried to divide by ZERO.')


print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))