#Decorators are used to modify or extend the behavior of a function without changing its source code.


def main_welcome(func):
    def sub_webcome_method():
        print("Welcom to the advance python course")
        func()
        print("Please learn these concepts property")

    return sub_webcome_method()



@main_welcome
def course_intro():
    print("This is an advanced python cource")

