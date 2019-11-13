import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
message = 'It was a '
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
# count1=pprint.pformat(count)
pprint.pprint(count)
