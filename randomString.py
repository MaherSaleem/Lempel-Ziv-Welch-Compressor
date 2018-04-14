import string
import random


def id_generator(size=6, chars=string.digits + string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))

print(id_generator(10, 'm'))
# print('Iam maher ' * 10000000)