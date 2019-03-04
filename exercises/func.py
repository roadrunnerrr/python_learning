message = input('Enter some message here: ')
print(message)

count = int(input('Enter the number of times to repeat the message'))
print(count)

def msg(message, count):
    print(f'{message * count}')

msg(message, count)
