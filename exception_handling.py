## Exception hand
# try:
#     result = 1/0

# except ZeroDivisionError as e:
#     print(e)
#     print('Please enter the denominator greater that 0')


#### File handling and Exception Handling
import os
try:
    file = open('sample.txt', 'r')
    content = file.read()
    print(content)

except FileNotFoundError:
    print("The file does not exists")

finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print('File close')