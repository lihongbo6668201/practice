def printPicNic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
        #print(k.rjust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sand': 4, 'apple': 12, 'cups': 4, 'cookies': 800}
printPicNic(picnicItems, 12, 5)
printPicNic(picnicItems, 20, 6)
