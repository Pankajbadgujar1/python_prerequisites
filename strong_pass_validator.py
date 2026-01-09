def is_strong_password(password):
    if len(password)<8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()-+' for char in password):
        return False
    return True

# calling function

print(is_strong_password("wekPass"))
print(is_strong_password("strongpPass23#$"))