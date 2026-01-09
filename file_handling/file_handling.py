import os
## working with text files


file_path = os.path.join(os.path.dirname(__file__), 'example.txt')

# with open(file_path, 'r') as file:
#     for line in file:
#         print(line)


# with open('example.txt','r'):
#     file.write('Hello World\n')
#     file.write('This is new line')

# with open(file_path, 'w') as file:
#     file.write('Hello World\n')
#     file.write('This is new line')


# with open(file_path, 'a') as file:
#     file.write("Append operation taking place! \n")


lines =['First line \n', 'Save line\n', 'Third line \n']
with open(file_path, 'a') as file:
    file.writelines(lines)

   

with open(file_path, 'r') as file:
    for line in file:
        print(line)

## Working with binary file ....