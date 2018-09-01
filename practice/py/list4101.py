def show(list1):
    len1=len(list1)
    for idx in range(0,len1 - 1):
        print( list1[idx] + ', ', end='' )
    print('and ' + list1[len1-1])

spam=['apples', 'bananas', 'tofu', 'cats']         
show(spam)

