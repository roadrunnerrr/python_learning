import os
import math

print(f'The PI equals to: {math.pi}')

digits = int(os.getenv('DIGITS') or 10)

my_float = round(math.pi, digits)

print(f'PI rounded to {digits} is {my_float}')


