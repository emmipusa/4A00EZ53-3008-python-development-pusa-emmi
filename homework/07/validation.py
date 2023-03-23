import string_helper

def is_name(name):
    if len(name) < 2:
        return False
    for char in name:
        if char.isdigit():
            return False
    return True

print(is_name)