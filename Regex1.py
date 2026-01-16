# def isPhoneNumber(number):
#     if len(number) != 12:
#         return False
#     for i in range(0,3):
#         if not number[i].isdecimal():
#             return False
#     if number[3] != '-':
#         return False
#     for i in range(4,7):
#         if not number[i].isdecimal():
#             return False
#     if number[7] != '-':
#         return False
#     for i in range(8,12):
#         if not number[i].isdecimal():
#             return False
#     return True
#
# ##print(isPhoneNumber('hello'))
# ##message = 'Call me at 455-455-4455 tomorrow, if not 999-999-9999. Thank you'
#
# message = 'Call me at 455-455-44 tomorrow, if not 999-999-99. Thank you'
# foundNumber = False
# for i in range(len(message)):
#     chunk = message[i:i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: '+ chunk)
#         foundNumber = True
# if not foundNumber:
#     print('Couldn\'t find any phone numbers.')


import re
message = 'Call me at 455-455-4455 tomorrow, if not 999-999-9999. Thank you'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
##mo = phoneNumRegex.search(message)

print(phoneNumRegex.findall(message))
##print(mo.group())

