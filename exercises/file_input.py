import io

f = input('Enter file name: ').strip()
print(f)

print('Enter file content \n')

with open(f, 'w') as file:
    eof = False
    lines = []
    while not eof:
        line = input()
        if line.strip():
            lines.append(f'{line}\n')
        else:
            eof = True

    file.writelines(lines)
    print(f'Content written to {f}')

