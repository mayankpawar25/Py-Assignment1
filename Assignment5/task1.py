#Create a Dictionary of Student Marks
studentInfo = {'Mike': 95, 'Alice': 85, 'Logan': 75}
userInput = input("Enter the student's name: ")

'''
try:
    score = studentInfo[str(userInput)]
    print("{}'s marks: {}" . format(userInput, str(score)))
except KeyError:
    print('Student not found')
'''

if studentInfo.get(str(userInput)):
    score = studentInfo[str(userInput)]
    print("{}'s marks: {}" . format(userInput, str(score)))
else:
    print('Student not found')
