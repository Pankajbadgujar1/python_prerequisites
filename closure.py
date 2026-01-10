# closure 
# method within a method 

# def main_welcome(msg):
#     def sub_webcome_method():
#         print("Welcom to the advance python course")
#         print(msg)
#         print("Please learn these concepts property")

#     return sub_webcome_method()

# obj = main_welcome("Hello")

## replace func with inbult function print
# def main_welcome(func):
#     def sub_webcome_method():
#         print("Welcom to the advance python course")
#         func(" This is welcome to function.....")
#         print("Please learn these concepts property")

#     return sub_webcome_method()

# obj = main_welcome(print)

def main_welcome(func,lst):
    def sub_webcome_method():
        print("Welcom to the advance python course")
        print(func(lst))
        print("Please learn these concepts property")

    return sub_webcome_method()

obj = main_welcome(len,[1,2,3,4,5,6])
