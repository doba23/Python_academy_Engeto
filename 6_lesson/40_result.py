def my_all(my_list):
    for item in my_list:
        if not item:
            return False
    return True

print(my_all(''))
