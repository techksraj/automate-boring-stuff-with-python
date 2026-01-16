"""

**********
*        *
*        *
*        *
**********


"""

# def boxPrint(symbol, width, height):
#     if len(symbol) != 1:
#         raise Exception('"Symbol" needs to be a string of length 1')
#     if (width < 2) or (height < 2):
#         raise Exception('"Height" or "Width" needs to be a greater than 2')
#     print(symbol * width)
#
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#
#     print(symbol * width)
#
# boxPrint('*', 1, 5)
#
# boxPrint('O', 50, 10)


market_2nd = {'ns': 'green', 'ew': 'red'}

def switchlights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


print(market_2nd)
switchlights(market_2nd)
print(market_2nd)