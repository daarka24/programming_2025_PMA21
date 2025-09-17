infile = open('first.txt', 'r')
lines = infile.readlines()
infile.close()

outfile = open('second.txt', 'w')

for line in lines:
    line = line.strip()

    if '+' in line:
        parts = line.split('+')
        operation = '+'
    elif '-' in line:
        parts = line.split('-')
        operation = '-'
    elif '*' in line:
        parts = line.split('*')
        operation = '*'
    elif '/' in line:
        parts = line.split('/')
        operation = '/'
    else:
        continue

    try:
        firstvector = [float(x) for x in parts[0].strip().strip('()').split(',')]
        secondvector = [float(x) for x in parts[1].strip().strip('()').split(',')]
    except ValueError:
        print(f"Skipping invalid line: {line}")
        continue

    result = []

    for i in range(len(firstvector)):
        a = firstvector[i]
        b = secondvector[i]

        if operation == '+':
            result.append(a + b)
        elif operation == '-':
            result.append(a - b)
        elif operation == '*':
            result.append(a * b)
        elif operation == '/':
            if b == 0:
                result.append(float('inf'))
            else:
                result.append(a / b)

    result = tuple(result)

    output_line = f"{firstvector} {operation} {secondvector} = {result}"

    outfile.write(output_line + '\n')

    print(output_line)

outfile.close()