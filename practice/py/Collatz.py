import sys


def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int(number * 3 + 1)


print('Enter a num: ')

try:
    num = int(input())
except ValueError:
    print('Error: invalid argument')
    sys.exit()

while num != 1:
    num = collatz(num)
    print(str(num))
