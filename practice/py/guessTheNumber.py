import random,sys

rnum = random.randint(1,20)

for idx in range(1,7):
    print('enter a num:')
    inum = int(input());

    if inum < rnum:
        print('low')
    elif inum > rnum:
        print('hign')
    else:
        print('niubi, ' +str(idx) +' times')
        sys.exit()

print('you are laji, the answer is ' +str(rnum))
