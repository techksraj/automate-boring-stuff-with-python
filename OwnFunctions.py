# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there!')
#
# hello()
# hello()
# hello()


# def hello(name):
#     print('Hello ' + name + '!')
#
# hello('Alice')
# hello('Raj')

# def plusOne(number):
#     return number + 1
#
# newNumber = plusOne(5)
# print(newNumber)


import random

spam = random.randint(1, 10)
print('spam value is: ' + str(spam))
if spam == 1:
    print('Random value was: ' + str(spam))
elif spam ==2:
    print('Random value was 2 : ' + str(spam))
elif spam ==3:
    print('Random value was 3 : ' + str(spam))
elif spam > 4:
    print('Random value was 5 6 7 8 9 10 : ' + str(spam))