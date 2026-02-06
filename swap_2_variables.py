
try:
    x = int(input('Enter a value for first variable'))
    y = int(input('Enter the value for second variable'))
    print(f"Before swap: x = {x} and y = {y}")
    temp = x
    x = y
    y = temp
    print(f"After swap: x = {x} and y = {y}")
except:
    print('Could not convert the input variable to int')
else:
    print('No error occured during program execution')
finally:
    print('End of the program! Thank you!')