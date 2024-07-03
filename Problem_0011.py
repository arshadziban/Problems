#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def copy_string(string, n):
    return string * n

string = input("Enter a string: ")
n = int(input("Enter a non-negative integer: "))
print(copy_string(string, n))