#Read File and handle errors

try:
    file = open('file1.txt', 'r')
    print("Reading file content:")
    for i, line in enumerate(file, 1):
        print('Line {}: {}'.format(i, line.strip()))
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
