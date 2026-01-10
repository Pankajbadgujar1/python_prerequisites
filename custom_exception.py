
# custom exception

class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter the year of birth: "))
age = 2024 - year

try:
    if age<=30 and age>= 20:
        print("The age is valid so you can apply for the exam")

    else:
        raise dobException
except dobException:
    print("Your age should be greater than 20 or less than 30 ")

