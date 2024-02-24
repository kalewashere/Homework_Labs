"""Write a quiz function that takes two arguments - one quiz question and the question's correct answer.

In your quiz function, you will print the question, and ask the user for the answer. If the user gets the answer
correct, print a success message. Else, print a message with the correct answer.   Your function does not need to
return anything.

Create a main function. From your main function, call your quiz function twice. So your program will ask the user one
question, verify the answer, ask the user another question, verify that answer. Here's some suggestions for questions
and their answers,

Q: Which planet is closest to the sun?  A: Mercury
Q: Who painted the Mona Lisa? A: Leonardo da Vinci"""

answer_1 = input('What is the capital of Japan? ')

if answer_1.upper() != 'TOKYO':
    print('Incorrect. The capital of Japan is Tokyo. ')
else:
    print(f'Correct! Next question.')

answer_2 = input('What is the capital of Minnesota? ')

if answer_2.upper() != 'ST PAUL':
    print('Incorrect. The capital of Minnesota is St. Paul')
else:
    print('Correct!')

