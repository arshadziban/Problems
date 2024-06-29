# Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

def file_name():
    file_name = input("Enter your file name: ")
    file= file_name.split(".")
    print("The extension of the file is: ", file[1])
file_name()