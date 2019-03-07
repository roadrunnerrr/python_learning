import sys
import argparse

parser = argparse.ArgumentParser(description='Receives a file_name and line_number as command line parameters.')
parser.add_argument('file', help='the file to read')
parser.add_argument('--line', '-l', help='line number to print')

args = parser.parse_args()
line = int(args.line) - 1

#print(line)

try:
    f = open(args.file)
except FileNotFoundError as err:
    print(f'Error: {err}')
    sys.exit(1)
else:
    with f:
        try:
            s = f.readlines()[line]
        except IndexError as err2:
            print(f'Error: {err2}')
        else:
            print(s)
