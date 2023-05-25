import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

for n in range(5):
    password = ''
    for i in range(6):
        password += random.choice(chars)
    print(password)