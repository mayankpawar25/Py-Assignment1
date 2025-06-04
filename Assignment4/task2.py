# Write and Append Data to a file

# Write a user input to a file
file = open('output.txt', 'w')
user_input = input("Enter text to write to the file: ")
file.write(user_input + '\n')
print("Data successfully written to output.txt")
file.close()

# Append data to the file
file = open('output.txt', 'a')
user_input = input("Enter addtional text to append: ")
file.write(user_input + '\n')
print("Data successfully appended")
file.close()

# Read data from the file
file = open('output.txt', 'r')
print('Final content of output.txt: ')
print(file.read())
file.close()

