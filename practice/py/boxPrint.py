def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')
    print(symbol * width ) 

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


testPara = [('*', 4,  4), ('0', 20, 5), ('x', 1, 3), 
            ('ZZ',3,  3), ('p', 4,  5), ('-', 3, 4),
            ('+', 2,  2), ('j', 2, 10), ('@', 6, 6)]
# for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
for sym, w, h in testPara:
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))
