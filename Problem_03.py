# Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
def reverse_name(first_name, last_name):
    return last_name + " " + first_name 

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(reverse_name(first_name, last_name))
